from django.shortcuts import render, redirect
from .models import  Dojo, Ninja

# Create your views here.
def main(request):
    alldojo=Dojo.objects.all()
    context={
       "alldojoinDB": alldojo
           }
    return render(request, 'index.html', context)
    

def insdojo(request):
    print(request.POST)
    dname=request.POST['name']
    dcity=request.POST['city']
    dstate=request.POST['state']

    Dojo.objects.create(name=dname, city=dcity,state=dstate)

    return redirect('/')

def insninja(request):
       selected_dojo=request.objects.get(id= request.POST['dojo_id'])
       Ninja.objects.create
       first_name=request.POST['first_name']
       last_name=request.POST['last_name']
       dojo=selected_dojo      
       return redirect('/')
    



# def getdojo(request):
#     alldojo=Dojo.objects.all()
#     context={
#         "alldojoinDB": alldojo
#           }
#     return render(request, 'index.html', context)

def getninja(request):
    allninja=Ninja.objects.all()
    context={
        "allninjainDB": allninja
          }
    return render(request, 'index.html', context)
