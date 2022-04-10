from ast import Pass
from multiprocessing import context
import re
from django.shortcuts import render, redirect
from django.contrib import messages
from Fav_Books import models
from .models import *
import bcrypt 


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()     
    print(pw_hash) 
    info=request.POST
    User.objects.create(first_name= info['first_name'],last_name=info['last_name'],email=info['email'],password=pw_hash)
    return redirect ('/')


def Log(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    user =User.objects.get(email=request.POST['email'])
    if user is not None:
        temp=user
        if bcrypt.checkpw(request.POST['password'].encode(), temp.password.encode()):
            request.session['first_name']=temp.first_name
            request.session['id']=temp.id
            request.session['email']=temp.email #hana
            return redirect('/addbook')
    return redirect('/')

def book(request):
    we=User.objects.get(id=request.session['id'])
    book=Book.objects.all() 
    users=User.objects.all()
    context={'user': we,
    'books': book,
    'y':users

}
    return render(request,'addbook.html', context)

def bookadd(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    info=request.POST
    #request.session['email'] =hana
    favuser=User.objects.get(id=request.session['id'])  #email =  hana
    Book.objects.create(Btitle=info['Btitle'], Bdesc=info['Bdesc'], Bupload=favuser)
    boo1=Book.objects.last()
    favuser.fusers.add(boo1)
    return redirect('/addbook')

def edit(request,id):
    book=Book.objects.get(id=id)
    user=User.objects.get(id=request.session['id'])
    context={'user': user,
    'book': book,
    }
    return render(request,'editbook.html', context )

def update(request,id):
    Selected=Book.objects.get(id=id)
    Selected.Btitle=request.POST['Btitle']
    Selected.Bdesc=request.POST['Bdesc']
    Selected.save()
    return redirect('/addbook')

def addfav(request, book_id):
    user1=User.objects.get(id=request.session['id'])
    selected_book = Book.objects.get(id=book_id)
    user1.fusers.add(selected_book)
    return redirect('/addbook')

def remfav(request,book_id):
    user_id=request.session['id']
    selected_book = Book.objects.get(id=book_id)
    thisuser=User.objects.get(user_id)
    selected_book.user_who_like.remove(thisuser)
    return redirect('/update')

def logout(request):
    request.session.clear()
    return redirect('/')



# def Log(request):
#     log=models.log_user(request.POST)
#     return redirect ('/')
