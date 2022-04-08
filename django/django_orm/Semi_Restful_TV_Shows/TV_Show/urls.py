from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.shows),
    path('new',views.new), # a route that renders the page that contains a form 
    path('create_show',views.create_show), #process the info from the form after submit
    path('edit_show/<int:id>', views.edit_show), #this route will render the edit form
    path('edit',views.edit_info),
    path('show_details/<int:id>',views.showD),
    path('delete/<int:id>',views.delete),
   # path('',include('TV_Show.urls')),
    #path('admin/', admin.site.urls),
]
