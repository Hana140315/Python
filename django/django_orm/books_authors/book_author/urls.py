from django.db import models

# Create your models here.
from django.urls import path, include

from book_author import views

urlpatterns = [
    path('',views.index),
    path('book', views.instbook),
    path('book/<int:id>',views.selectbook),
    path('addauthor/<int:id>',views.addauthor),
    path('author', views.author),
    path('insauthor',views.insauthor),
    path('author/<int:id>',views.selectauthor)
    #path('', include('book_author.urls')),
   # path('admin/', admin.site.urls),
]
