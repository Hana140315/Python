from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.result),
    path('result', views.showdata)
    
    #path('admin/', admin.site.urls),
]
