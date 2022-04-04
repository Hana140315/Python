from multiprocessing import context
from django.shortcuts import render
from .models import *
from . import models


# Create your views here.

def shows(request):
    show_list=models.listofShow()
    context = {
        "shows" : show_list,
    }
    return render(request,'shows.html',context)

