from django.db import models

# Create your models here.
class Show(models.Model):
    title=models.CharField(max_length=100)
    network=models.CharField(max_length=10)
    release_date=models.DateField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

def listofShow():
    return Show.objects.all()