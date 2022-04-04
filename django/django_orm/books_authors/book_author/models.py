
from django.db import models

class Book(models.Model):
    title= models.CharField(max_length=255)
    desc= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


class Author(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    notes=models.TextField(default="Book Authour Assg")
    books=models.ManyToManyField(Book, related_name="authors")
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


def one_book(book_id): #id = book_id --> from views one_book(book_id)
    return Book.objects.get(id=book_id)

def add_author(info,book_id):
    book = Book.objects.get(id=book_id)	
    auth= Author.objects.get(id=info['addauthor'])	
    book.authors.add(auth)
    return 

def one_author(author_id):
    return Author.objects.get(id=author_id)

def add_book(info,author_id):
    auth= Author.objects.get(id=author_id)
    book = Book.objects.get(id=info['selectauthor'])
    auth.books.add(book)
    return 
