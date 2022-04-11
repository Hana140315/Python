from django.urls import path
from wallApp import views

urlpatterns = [
    path('',views.index),
    path('addPost',views.addpost),
    path('addcomment/<int:userid>/<int:mid>', views.addcomment)
]