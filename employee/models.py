from django.db import models

# Create your models here.

from datetime import datetime
class Department(models.Model):
    dep_name =models.CharField(max_length=40)
    dep_salary =models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.dep_name

class Employee(models.Model):
    GENDER_TYPE=[
        ('M','MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHER'),
    ]
    emp_name =models.CharField(max_length=100)
    emp_photo= models.ImageField(upload_to='emplyees_photo', default='emp_avtar.jpg')
    emp_address = models.TextField(max_length=200)
    emp_mobile =models.CharField(max_length=10)
    emp_email = models.EmailField(default='xyz@gmail.com')
    emp_type = models.ForeignKey(Department, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_TYPE, max_length=8)
    emp_joining_date = models.DateTimeField(auto_now_add=True)
    emp_update_date = models.DateTimeField(auto_now=True)
    emp_dob = models.DateField(default=datetime.today)
    emp_block =models.BooleanField(default=True)

    def __str__(self):
        return self.emp_name

class Attendance(models.Model):
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    availablity =models.BooleanField(default=True)
    attendance_date = models.DateTimeField(default=datetime.today)

    def __str__(self):
        if self.availablity==True:
            return str(self.employee.emp_name)+" : present"
        else:
            return str(self.employee.emp_name)+" : upsent"


class Payment_Employee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    amount =models.DecimalField(max_digits=8, decimal_places=2)
    desc = models.TextField(default="optional")

#


