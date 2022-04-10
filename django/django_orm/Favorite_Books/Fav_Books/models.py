from django.db import models
import re


# Create your models here.
class LogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 3 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters" 
        if postData['password'] != postData['conf_password']:
            errors["conf_password"] = "Not confirm password"    
        return errors
    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password'] = "Blog password should be at least 8 characters"
           
        return errors
    def book_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['Bdesc']) < 5:
            errors["Bdesc"] = "Description should be at least 5 characters"
        return errors
    
class User(models.Model):
        first_name=models.CharField(max_length=45)
        last_name=models.CharField(max_length=45)
        email=models.CharField(max_length=50 , default="hana78@gmail.com")
        password=models.CharField(max_length=16)
        
        created_at= models.DateTimeField(auto_now_add=True)
        update_at=models.DateTimeField(auto_now=True)
        objects=LogManager()

class Book(models.Model):
        Btitle=models.CharField(max_length=255)
        Bdesc=models.TextField()
        Bupload=models.ForeignKey(User, related_name="books", on_delete=models.CASCADE)
        Busers=models.ManyToManyField(User, related_name="fusers")
        created_at= models.DateTimeField(auto_now_add=True)
        update_at=models.DateTimeField(auto_now=True)
        objects=LogManager()

###### Method to be used  in the application ######








