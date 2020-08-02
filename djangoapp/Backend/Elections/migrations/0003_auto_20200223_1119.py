# Generated by Django 3.0.3 on 2020-02-23 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elections', '0002_auto_20200223_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voteingcampaign',
            name='conductedFor',
        ),
        migrations.AddField(
            model_name='candidate',
            name='aboutMySelf',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='motivation',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='wChanges',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='firstName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='lastName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='voteingcampaign',
            name='level',
            field=models.CharField(choices=[('SCR', 'Class representative'), ('SPS', 'College president')], max_length=100),
        ),
    ]
