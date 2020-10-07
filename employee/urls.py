

from django.urls import path
from . import views

# def homepage(request):
#     return HttpResponse('Hello Django')


urlpatterns = [
    path('add_attendace/', views.add_attendace, name="add_attendace"),
    path('save_attendece/', views.save_attendece, name="save_attendece"),
    path('', views.dashboard, name="dashboard"),
    path('week_attendace/', views.week_attendace, name="week_attendace"),
    path('emp_payment/', views.emp_payment, name="emp_payment"),

]
