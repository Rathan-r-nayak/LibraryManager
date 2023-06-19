from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def welcomePage(request):
    template=loader.get_template("loginApp/index.html")
    return render(request,"loginApp/index.html")

def signinPage(request):
    template=loader.get_template("loginApp/signinPage.html")
    # return HttpResponse(template.render())
    return render(request,"loginApp/signinPage.html")

def signupPage(request):
    template=loader.get_template("loginApp/signupPage.html")
    # return HttpResponse(template.render())
    return render(request,"loginApp/signupPage.html")
