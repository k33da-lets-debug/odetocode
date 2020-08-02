from django.contrib import admin
from .models import Department,Class,Student,VoteingCampaign,Candidate,Vote


class DepartmentAdmin(admin.ModelAdmin):
    list_display=('id','departmentName')
    list_display_links=('id','departmentName')
    search_fields = ('id','departmentName')
    list_per_page=25

class ClassAdmin(admin.ModelAdmin):
    list_display=('id','department','year','division')
    list_display_links=('id','department','year','division')
    search_fields = ('id','department','year','division')
    list_per_page=25

class StudentAdmin(admin.ModelAdmin):
    list_display=('id','firstName','lastName','gender','email','rollNo','departmentDetails','classDetails')
    list_display_links=('id','firstName','lastName','gender','email','rollNo')
    search_fields = ('id','firstName','lastName','gender','email','rollNo')
    list_filter = (
        ('classDetails', admin.RelatedOnlyFieldListFilter),
    )
    list_per_page=25

class VoteingCampaignAdmin(admin.ModelAdmin):
    list_display=('id','departmentDetails','classDetails','level','conducted_by','datetime')
    list_display_links=('id','departmentDetails','classDetails','level','conducted_by','datetime')
    search_fields = ('id','departmentDetails','classDetails','level','conducted_by','datetime')
    list_per_page=25

class CandidateAdmin(admin.ModelAdmin):
    list_display=('id','candidate','votingCampaign','candidate')
    list_display_links=('id','votingCampaign','candidate')
    search_fields = ('id','votingCampaign','candidate')
    list_filter = (
        ('votingCampaign', admin.RelatedOnlyFieldListFilter),
    )
    list_per_page=25

class VoteAdmin(admin.ModelAdmin):
    pass
# Register your models here.

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Class,ClassAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(VoteingCampaign,VoteingCampaignAdmin)
admin.site.register(Candidate,CandidateAdmin)
admin.site.register(Vote)

