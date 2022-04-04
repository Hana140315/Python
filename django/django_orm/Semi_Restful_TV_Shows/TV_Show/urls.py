from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('shows', views.shows)
   # path('',include('TV_Show.urls')),
    #path('admin/', admin.site.urls),
]
