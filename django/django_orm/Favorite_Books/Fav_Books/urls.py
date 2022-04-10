from django.db import models

# Create your models here.
from django.urls import path

from Fav_Books import views

urlpatterns = [
    path('',views.index),
    path('register', views.register),
    path('login',views.Log),
    path('addbook', views.book), #display all books + the form t0 add a book
    path('newbook',views.bookadd), #add a new book to DB (route that process the info_)
    path('addbook/<int:id>', views.edit), #display the book info and the edit form for title and desc
    path('<int:id>/update',views.update ), #process the update info 
    path('add_fav/<int:book_id>', views.addfav), 
    path('rem_fav/<int:book_id>', views.remfav),#will add a book to the "fav book list" of the user
    path('logout', views.logout),

]