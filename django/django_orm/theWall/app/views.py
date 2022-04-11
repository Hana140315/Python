from django.shortcuts import render,HttpResponse,redirect
from app.models import User
from django.contrib import messages
from app import models
from wallApp import views

# Create your views here.
def index(request):
    if 'email' in request.session:
         del request.session['email']
    else:
        print("key 'key_name' does NOT exist")
       

    return render(request,'LoginAndRegistration.html')
def registration(request):
    errors = User.objects.registration_validator(request.POST)
        
    if len(errors) > 0:
        context={
            'flag':0
        }
       
        for key, value in errors.items():
            messages.error(request, value)
        
        return render(request, 'LoginAndRegistration.html',context)
    else:
        models.register(request.POST)
        return render(request,'LoginAndRegistration.html')
def login(request):
    errors2 = User.objects.login_validator(request.POST)
        
    if len(errors2) > 0:
        context={
            'flag':1
        }
       
        for key, value in errors2.items():
            messages.error(request, value)
       
        return render(request, 'LoginAndRegistration.html',context)
    else:
        flag=models.confermLogin(request.POST)
        if(flag):
            request.session['email']=request.POST['email']
            context={
                'user':User.objects.get(email=request.session['email'])
            }
            return redirect('/sucsess')
        else:
            return redirect('/')
def sucsess(request):
    return views.index(request)