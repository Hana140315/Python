from django.shortcuts import render, redirect
from .models import Users

# Create your views here.
def getUsers(request):
    allusers=Users.objects.all()
    context={
        "allusersinDB": allusers  
          }
    return render(request, 'index.html', context)

def insertUser(request):
    print(request.POST)
    fname=request.POST['first_name']
    lname=request.POST['last_name']
    email=request.POST['email']
    age=request.POST['age']
    Users.objects.create(first_name=fname, last_name=lname,email=email, age=age)

    return redirect('/')