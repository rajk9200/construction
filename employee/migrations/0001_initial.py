# Generated by Django 2.2.10 on 2020-05-23 09:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=40)),
                ('dep_salary', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_photo', models.ImageField(default='emp_avtar.jpg', upload_to='emplyees_photo')),
                ('emp_address', models.TextField(max_length=200)),
                ('emp_mobile', models.CharField(max_length=10)),
                ('emp_email', models.EmailField(default='xyz@gmail.com', max_length=254)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('O', 'OTHER')], max_length=8)),
                ('emp_joining_date', models.DateTimeField(auto_now=True)),
                ('emp_dob', models.DateField(default=datetime.datetime.today)),
                ('emp_block', models.BooleanField(default=True)),
                ('emp_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('availablity', models.BooleanField(default=True)),
                ('attendance_date', models.DateTimeField(verbose_name=datetime.datetime.today)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
        ),
    ]
