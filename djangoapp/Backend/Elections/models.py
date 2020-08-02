from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.conf import settings


#choices
ROLE_CHOICES = (
    ('S', 'Student'),
    ('SCR', 'Class representative'),
    ('SPS','College president'),
    ('Class Representative','Class Representative'),
    ('College president','College president'),
)

LEVEL_CHOICES = (
    ('CLS', 'Class level'),
    ('CLG', 'College level'),
)

YEAR_CHOICES = (
    ('FY', 'First year'),
    ('SY', 'Second year'),
    ('TY', 'Third year'),
    ('FRY', 'Fourth year'),
)

DIVISION_CHOICES = (
    ('MCA1', 'MCA morning'),
    ('MCA2', 'MCA afternoon'),
    ('D1', 'D1'),
    ('D2', 'D2'),
    ('Some department', 'Some department'),
    ('EXTC', 'Electronics'),
)

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

# Create your models here.
class Department(models.Model):
    departmentName = models.TextField(max_length=100)
    def __str__(self):
        return self.departmentName
    
    class Meta:
        verbose_name_plural = "Departments"

class Class(models.Model):
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    year = models.CharField(max_length=100, choices=YEAR_CHOICES)
    division = models.CharField(max_length=100, choices=DIVISION_CHOICES)
    def __str__(self):
        return self.department.departmentName + " " +self.year + " " + self.division

    class Meta:
        verbose_name_plural = "Classes"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    phoneNo = PhoneNumberField( null=True, blank=True, unique=True)
    departmentDetails = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    classDetails = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    rollNo = models.IntegerField()
    birthDate = models.DateField()
    role=models.CharField(max_length=100, choices=ROLE_CHOICES)
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = "Student details"

class VoteingCampaign(models.Model):
    nameOfCampaign = models.CharField(max_length=200,default='')
    shortDescription = models.CharField(max_length=200,default='')#added
    departmentDetails = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    classDetails = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    level=models.CharField(max_length=100, choices=ROLE_CHOICES[1:])
    conducted_by=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    datetime=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nameOfCampaign+" "+self.departmentDetails.departmentName + " " + self.classDetails.year + " " + self.classDetails.division

    class Meta:
        verbose_name_plural = "Voting campaign details"

class Candidate(models.Model):
    votingCampaign = models.ForeignKey(VoteingCampaign,on_delete=models.CASCADE)
    candidate = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    displayImage = models.ImageField(null=True, blank=True,upload_to='candidate_display_image/', height_field=None, width_field=None, max_length=100)
    short_description = models.TextField(max_length=200,null=True, blank=True)
    aboutMySelf = models.TextField(max_length=200,null=True, blank=True)
    motivation = models.TextField(max_length=200,null=True, blank=True)
    wChanges = models.TextField(max_length=200,null=True, blank=True)
    def __str__(self):
        return self.candidate.firstName+" "+self.candidate.lastName

    class Meta:
        verbose_name_plural = "Participating candidates"

class Vote(models.Model):
    votingCampaign = models.ForeignKey( VoteingCampaign , on_delete=models.DO_NOTHING)
    voteForCandidate = models.ForeignKey( Candidate , on_delete=models.DO_NOTHING) #only associated with that voting
    vote = models.BooleanField()
    votedBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Voting details"

