# Generated by Django 3.0.3 on 2020-02-23 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('FY', 'First year'), ('SY', 'Second year'), ('TY', 'Third year'), ('FRY', 'Fourth year')], max_length=100)),
                ('division', models.CharField(choices=[('MCA1', 'MCA morning'), ('MCA2', 'MCA afternoon'), ('D1', 'D1'), ('D2', 'D2'), ('EXTC', 'Electronics')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentName', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.TextField(max_length=100)),
                ('lastName', models.TextField(blank=True, max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNo', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True)),
                ('rollNo', models.IntegerField()),
                ('birthDate', models.DateField()),
                ('displayImage', models.ImageField(blank=True, null=True, upload_to=None)),
                ('role', models.CharField(choices=[('S', 'Student'), ('SCR', 'Class representative'), ('SPS', 'College president')], max_length=100)),
                ('classDetails', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Elections.Class')),
                ('departmentDetails', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Elections.Department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Elections.Department'),
        ),
    ]
