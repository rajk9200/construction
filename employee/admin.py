from django.contrib import admin

# Register your models here.

from .models import Employee,Department,Attendance
from .models import Payment_Employee
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Attendance)
admin.site.register(Payment_Employee)

