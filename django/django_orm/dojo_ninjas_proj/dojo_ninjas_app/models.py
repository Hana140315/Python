from ssl import create_default_context
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Dojo(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=2)
    desc=models.CharField(max_length=45, default="Majed_Assg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ninja(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    dojo=models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# def addojo(info):
#     #info = request.POST
#     Dojo.objects.create(first_name=info['name'], city=info['city'], state=info['state'])

# def addninja(info):
#     Ninja.objects.create(first_name=info['first_name'], last_name=info['last_name'], dojo=info['dojo'])


# def list_all_dojo_ninja():
#     for dojo in Dojo.objects.all():
#         for  nin in Ninja.object.all():    
#             return Dojo.objects.all(Ninja.objects.get(dojo=Dojo.objects.get(name="")))