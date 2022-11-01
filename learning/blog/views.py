from django.shortcuts import render
from django.http import HttpResponse
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
