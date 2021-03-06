# Generated by Django 4.0.1 on 2022-03-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0005_studentofferletterfee_student_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentPaymentReceive',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('installment_date', models.DateField()),
                ('installment_fees', models.CharField(max_length=255)),
                ('invoice_no', models.CharField(max_length=255)),
                ('note', models.CharField(max_length=255)),
            ],
        ),
    ]
