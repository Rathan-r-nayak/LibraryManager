from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def adminLoginPage(request):
    return render(request,"adminApp/adminLoginPage.html")

def adminPage(request):
    return render(request,"adminApp/adminPage.html")