from ast import Pass
from multiprocessing import context
import re
from django.shortcuts import render, redirect
from django.contrib import messages
from Log_Reg import models
from .models import *
import bcrypt 


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    errors = LogReg.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()     
    print(pw_hash) 
    info=request.POST
    LogReg.objects.create(first_name= info['first_name'],last_name=info['last_name'],email=info['email'],password=pw_hash)
    return redirect ('/')


def Log(request):
    errors = LogReg.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    user =LogReg.objects.get(email=request.POST['email'])
    if user is not None:
        temp=user
        if bcrypt.checkpw(request.POST['password'].encode(), temp.password.encode()):
            request.session['email']=temp.email    
            return redirect('/sucess')
    return redirect('/')

def ls(request):
    we=LogReg.objects.get(email=request.session['email'])
    context={'first_name': we.first_name}
    return render(request,'sucess.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')
    

# def Log(request):
#     log=models.log_user(request.POST)
#     return redirect ('/')