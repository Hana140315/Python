from django.db import models

# Create your models here.
from django.urls import path

from Log_Reg import views

urlpatterns = [
    path('',views.index),
    path('register', views.register),
    path('login',views.Log),
    path('sucess', views.ls),
    path('logout', views.logout)

]