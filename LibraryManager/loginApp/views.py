from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . import models

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



import pandas as pd
import numpy as np
import csv
def filldb(request):
    file = open("static/database_values.csv")
    # csvreader = csv.reader(file)
    df=pd.read_csv(file)
    for i in df.values:
        bid=i[0]
        title=i[1]
        author=i[2]
        year=i[3]
        summary=i[4]
        copies=i[5]
        book=models.Book(book_id=bid,title=title,pub_year=year,author=author,copies=copies,summary=summary)
        book.save()
    return HttpResponse("added values to database")
