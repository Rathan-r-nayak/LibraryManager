from django.urls import include,path
from . import views


urlpatterns=[
    path("",views.adminLoginPage,name="adminLoginPage"),
    path("adminSigninInput",views.adminSigninInput),
    path("adminPage/",views.adminPage),
    path("bookInput",views.bookInput),
]