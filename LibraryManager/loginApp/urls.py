from django.urls import include,path
from . import views


urlpatterns=[
    path("",views.welcomePage),
    path("signin/",views.signinPage),
    path("signup/",views.signupPage),
]