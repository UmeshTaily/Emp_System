from django.shortcuts import render, HttpResponse
from emp_app.models import Employee, Department, Role
from datetime import datetime
from django.db import models
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, 'index.html')

def view_emp(request):
    emps = Employee.objects.all()
    return render(request, 'view_emp.html', {'emps':emps})

def add_emp(request):
    validate = False
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        deptname = int(request.POST.get('deptname'))
        rolename = int(request.POST.get('rolename'))
        addtotable = Employee(first_name=first_name, last_name=last_name, phone=phone, dept_id=deptname, role_id=rolename, date=datetime.now())
        addtotable.save()
        validate = True
    return render(request, 'add_emp.html', {'validate':validate})

def remove_emp(request, emp_id=0):
    validate = False
    empall = Employee.objects.all()
    if emp_id != 0:
        emp = Employee.objects.get(id=emp_id)
        emp.delete()
        validate=True
    return render(request, 'remove_emp.html', {'empall':empall, 'validate':validate})

def filter_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        deptname = request.POST.get('deptname')
        rolename = request.POST.get('rolename')
        if first_name:
            emps = Employee.objects.filter(Q(first_name=first_name))
            # emps = Employee.objects.filter(Q(first_name=first_name), Q(last_name=last_name) , Q(dept__name=deptname) , Q(role__name=rolename))
        if last_name:
            emps = Employee.objects.filter(Q(last_name=last_name))
        if deptname:
            emps = Employee.objects.filter(Q(dept__name=deptname))
        if rolename:
            emps = Employee.objects.filter(Q(role__name=rolename))
        return render(request, 'view_emp.html', {'emps':emps})
    else:
        return render(request, 'filter_emp.html')