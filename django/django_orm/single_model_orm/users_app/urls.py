#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUsers),
    path('users',views.insertUser ),
    #path('admin/', admin.site.urls),
]
