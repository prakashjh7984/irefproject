# Generated by Django 4.0.1 on 2022-02-24 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0002_alter_collegedocument_eighth_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]