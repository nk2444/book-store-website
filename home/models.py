from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    date = models.DateTimeField()

 
    def __str__(self):
        return self.name
    
    
class Author(models.Model):
    name = models.CharField(max_length=250, blank=False)
    email=models.EmailField()
def __str__(self):
    return self.name

         
class Product(models.Model):
    book_title = models.CharField(max_length=250, blank=False)
    authors = models.ManyToManyField(Author, blank=True)
    pub_date = models.DateTimeField()
    price= models.IntegerField()
    image = models.ImageField(upload_to= "images", default="")
    
def __str__(self):
      return self.book_title 
