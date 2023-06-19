from django.urls import include,path
from . import views


urlpatterns=[
    path("",views.adminLoginPage),
    path("adminPage/",views.adminLoginPage),
]