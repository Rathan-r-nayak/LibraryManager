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



def search(request):
    search_query=request.GET['searchQuery']
    if(search_query==""):
        return redirect("homePage")
    if len(search_query)>80:
        allbooks=models.Schemes.objects.none()
    else:
        alltitle=models.Book.objects.filter(title__icontains=search_query)
        allauthor=models.Book.objects.filter(author__icontains=search_query)
        allsummary=models.Book.objects.filter(summary__icontains=search_query)
        allbooks=alltitle.union(allauthor,allsummary)



    context={'book':allbooks,
         'query':search_query,
        }
    return render(request,'studentApp/search.html',context)



def bookDetail(request,bookdet):
    bookOb=models.Book.objects.get(title=bookdet)
    # try:
    #     benftOb=models.Benifits.objects.filter(stitle=schmOb).values()
        
    # except:
    #     benftOb=None
    context={
        'book':bookOb,
    }
    template = loader.get_template('studentApp/bookDetail.html')
    return HttpResponse(template.render(context,request))