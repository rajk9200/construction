from django.shortcuts import render,HttpResponse,HttpResponseRedirect

# Create your views here.
from .form import  PaymentForm
from .models import Employee
from .models import Attendance,Payment_Employee
import json
from datetime import datetime,timedelta
from house_owner.models import Owner_pay
def add_attendace(request):
	context=dict()
	tdate =datetime.today()
	date_N_days_ago = datetime.today() - timedelta(days=1)
	ndate = date_N_days_ago
	emps=Employee.objects.all()
	attendacelist =Attendance.objects.filter(attendance_date__date=tdate)
	context['emps']=emps
	context['tdate']= tdate
	context['attendacelist']= attendacelist

	return render(request,"attendece.html",context)

def save_attendece(request):
	if request.is_ajax():
		data = json.loads(request.GET.get('data1', ''))
		if data:
			for em in data:
				print(data)
				print(em['id'],em['op'])
				if em['op']=="P":
					attendace =True
					emp=Employee.objects.get(id=em['id'])
					gotAt =Attendance.objects.filter(employee=emp,attendance_date__date=datetime.today())
					print(gotAt)
					if not gotAt:
						Attendance.objects.create(employee=emp, availablity=attendace)
				else:
					attendace = False
					return HttpResponseRedirect('save_attendece')

	return HttpResponse("Attendece saved")


def dashboard(request):
	context=dict()
	return render(request,"home/index.html",context)

def emp_payment(request):
	form =PaymentForm(request.POST or None)
	if form.is_valid():
		form.save()
		print('data save ho gya')
	data ={
		'form':form
	}
	return render(request,'payment.html',data)

def week_attendace(request):
	data = []
	tdate = datetime.today()
	date_N_days_ago = datetime.today() - timedelta(days=7)
	ndate = date_N_days_ago
	all_emp = Employee.objects.all()
	c = 0
	for em in all_emp:
		day = Attendance.objects.filter(employee=em, attendance_date__range=[ndate, tdate]).count()
		opay = Payment_Employee.objects.filter(employee=em, date__range=[ndate, tdate])
		cpay = 0
		for p in opay:
			cpay = cpay + float(p.amount)

		data.append([f"<img src='{em.emp_photo.url}' class='img_box'>", f"<a href='{em.id}'>{em.emp_name}</a>", em.emp_type, day,
					 float(day) * float(em.emp_type.dep_salary), cpay,
					 (float(day) * float(em.emp_type.dep_salary) - cpay)])
		c = c + 1
	total = 0.0
	paidc = Owner_pay.objects.all()
	for am in paidc:
		total = total + float(am.amount)

	context = {
		'data': data,
		'total': total
	}
	return render(request,'home/week_report.html',context)




