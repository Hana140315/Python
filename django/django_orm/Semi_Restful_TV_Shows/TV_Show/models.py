from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Blog first name should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Blog last name should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Blog password should be at least 8 characters" 
        return errors

# Create your models here.
class Show(models.Model):
    title=models.CharField(max_length=100)
    network=models.CharField(max_length=10)
    release_date=models.DateField()
    desc=models.TextField(max_length=500, default="This is Nice Show")
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects=ShowManager()




def listofShow():
    return Show.objects.all()

def newshow(info):
    Show.objects.create(title=info['title'],network=info['network'],release_date=info['release_date'],desc=info['desc'])

def oneshow(show_id):
    return Show.objects.get(id=show_id)

def editshow(info):
    this_show_id = info['show_id']
    print(this_show_id)
    editsh=Show.objects.get(id= this_show_id)
    editsh.title=info['title']
    editsh.network=info['network']
    editsh.release_date=info['release_date']
    editsh.desc=info['desc']
    editsh.save()
    return editsh

def delete1(info):
    # this_show_id = info['show_id']
    # print(this_show_id)
    delsh=Show.objects.get(id= info)
    # delsh.title=info['title']
    # delsh.network=info['network']
    # delsh.release_date=info['release_date']
    # delsh.desc=info['desc']
    delsh.delete()
    # return delsh