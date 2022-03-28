
import re
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse


# Create your views here.
def index(request):
    return HttpResponse("placeholder to display a new form to create a new blog ")
def root(request):
    return HttpResponse("Hana")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog ")
def create(request):
    return redirect("/")

def show(request,num):
    return HttpResponse(f"placeholder to display a new form to create a new blog {num}",num)
def edit(request, num):
    return HttpResponse(f"placeholder to edit blog {num}", num)
def destroy(request,num):
    return redirect("/blogs")

def jason(request):
    return JsonResponse({"title": "My_first_blog", "content":"lorem Majed Amira Hana Albidaq"})