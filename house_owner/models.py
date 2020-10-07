from django.db import models

# Create your models here
#
from datetime import datetime
class House_Owner(models.Model):
    GENDER_TYPE = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHER'),
    ]
    owner_name = models.CharField(max_length=100)
    owner_photo = models.ImageField(upload_to='emplyees_photo', default='emp_avtar.jpg')
    owner_address = models.TextField(max_length=200)
    owner_mobile = models.CharField(max_length=10)
    owner_email = models.EmailField(default='xyz@gmail.com')
    gender = models.CharField(choices=GENDER_TYPE, max_length=8)
    owner_work_start = models.DateTimeField(auto_now_add=True)
    owner_work_end = models.DateTimeField(default=datetime.today)
    owner_action = models.BooleanField(default=True)

class Owner_pay(models.Model):
    owner = models.ForeignKey(House_Owner, models.CASCADE)
    amount =models.DecimalField(max_digits=8, decimal_places=2)
    desc = models.TextField(default="optional")
    date = models.DateTimeField(default=datetime.today)