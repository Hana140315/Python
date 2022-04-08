from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from .models import *
from . import models



# Create your views here.

def shows(request):
    show_list=models.listofShow()
    context = {
        "shows" : show_list,
    }
    return render(request,'shows.html',context)

def new(request):

    return render(request,'new.html')

def create_show(request):
    print(request.POST)
    models.newshow(request.POST)
    return redirect('/')

def edit_show(request,id):
    context={
        'x' : models.oneshow(id) 
    }
    return render(request,'edit.html',context)
  
   
def  edit_info(request):
    #will got to database and will update the show passed to it
    showedit= models.editshow(request.POST)
    return redirect('/')
 
def showD(request,id):
    show_det=models.oneshow(id)
    context={
         'x' : models.oneshow(id) 
    }
    return render(request,'show_details.html',context)

def delete(request,id):
    # del1_id=request.POST['show.id']
    #will got to database and will update the show passed to it
    showdel= models.delete1(id)
    return redirect('/')