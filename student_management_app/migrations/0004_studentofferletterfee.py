# Generated by Django 4.0.1 on 2022-03-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0003_customuser_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentOfferLetterFee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('installment_date', models.DateField()),
                ('fees', models.CharField(max_length=255)),
                ('note', models.CharField(max_length=255)),
            ],
        ),
    ]
