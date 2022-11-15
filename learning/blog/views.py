from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def aboutUs(request):
    return render(request,"aboutUs.html")

def contactUs(request):
    data={
        "firstName":"Vraj",
        "lastName":"Patel"
    }
    return render(request,"contactUs.html",data)

def showEmployee(request):
    employees = Employee.objects.all().values()
    emp = Employee.objects.all().values_list()
    return render(request,"relationship/manyTomany.html",{'employees':employees,'emp':emp})