from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.template import loader
from . import models
from django.contrib.auth.models import User

# Create your views here.
def homePage(request):
    template=loader.get_template("loginApp/index.html")
    return render(request,"studentApp/homePage.html")