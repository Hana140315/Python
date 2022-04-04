from django.urls import path
from . import views
urlpatterns = [
    path('', views.main),
    path('addojo', views.insdojo),
    path('addninja', views.insninja),
    path('getninja', views.getninja)
   # path('admin/', admin.site.urls),
]
