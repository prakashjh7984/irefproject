# Generated by Django 4.0.1 on 2022-05-05 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0022_customuser_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentresult',
            name='total_max_marks',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
