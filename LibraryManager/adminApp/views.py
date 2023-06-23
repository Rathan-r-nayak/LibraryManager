from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.template import loader
from . import models
from django.contrib.auth.models import User

def adminLoginPage(request):
    return render(request,"adminApp/adminLoginPage.html")

def adminSigninInput(request):
    if request.method =='POST':
        uname=request.POST['uname']
        passwd=request.POST['passwd']
        print(uname,passwd)
        user=authenticate(username=uname,password=passwd)
        if user is not None:
            if(user.is_superuser):
                print("\n",user.username,"\n")
                login(request,user)
                messages.success(request,f"successfully logged in as {user}")
                return HttpResponseRedirect(f'./adminPage/')
        else:
            # messages.info(request,'invalid user')
            messages.error(request,f"failed to login")
            return redirect("adminLoginPage")



def adminPage(request):
    return render(request,"adminApp/adminPage.html")


def bookInput(request):
    pass