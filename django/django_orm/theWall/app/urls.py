from django.urls import path,include
from app import views
urlpatterns = [
    path('',views.index),
    path('registration',views.registration),
    path('login',views.login),
    path('sucsess',views.sucsess)
]