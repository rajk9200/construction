from django.contrib import admin

# Register your models here.
from .models import House_Owner,Owner_pay
admin.site.register(House_Owner)
admin.site.register(Owner_pay)