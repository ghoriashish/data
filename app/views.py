from django.shortcuts import render,HttpResponsePermanentRedirect,reverse
from .models import *
# Create your views here.
def indexpage(request):
    return render(request,"app/index.html")
def success(request):
    return render(request,"app/success.html")
def registarpage(request):
    id=request.POST['id']
    name=request.POST['name']
    dob=request.POST['dob']
    email=request.POST['email']
    password=request.POST['password']
    mobileno=request.POST['mobileno']
    salary=request.POST['salary']

    user=employee.objects.create(id=id,name=name,dob=dob,email=email,password=password,mobileno=mobileno,salary=salary)
    return HttpResponsePermanentRedirect(reverse('show'))
def show(request):
    alluser=employee.objects.all()
    return render(request,"app/success.html",{'key':alluser})