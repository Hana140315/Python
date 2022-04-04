#from turtle import tilt, title
from django.shortcuts import render, redirect
from book_author import models
from book_author.models import Book, Author


# Create your views here.
def index(request):
    context={
        'books':Book.objects.all()
        
    }
    return render(request,'book.html', context)

def instbook(request):
    Book.objects.create(
        title=request.POST['title'],
        desc=request.POST['desc']
    )
    return redirect ('/')

def selectbook(request,id):
    print("***",id)
    print(("$$$",type(id)))
#    selected_book=Book.objects.get(id=book_id)
    selected_book = models.one_book(id)
    Bauthors=Author.objects.all()
    context = {
        "this_book" : selected_book,
        "Bauthors"  :Bauthors,
    }
    return render (request,'Selectbook.html',context)

def addauthor(request, addA):
    selected_author=models.add_author(request.POST,addA)
    context ={
        'Bauthors' : selected_author
    }
    #return render (request,'Selectbook.html',context)
    return redirect('/book')

def author(request):
    context={
        'author':Author.objects.all()
        
    }
    return render(request,'author.html', context)

def insauthor(request):
    Author.objects.create(
       first_name=request.POST['first_name'],
       last_name=request.POST['last_name'],
       notes=request.POST['notes']
    )
    return redirect ('/author')
# Select add book to author
def selectauthor(request, id):
    selected_author = models.one_author(id)
    Abooks=Book.objects.all()
    context = {
        "this_author" : selected_author,
        "Abooks"  :Abooks,
    }
    return render (request,'SelectAuthor.html',context)
