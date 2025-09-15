from django.db import models 
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Author(models.Model): 
    name = models.CharField(max_length=200) 

class Book(models.Model):
    title = models.CharField(max_length=200)        
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=200)         
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=100)         
    library = models.OneToOneField(Library, on_delete=models.CASCADE)



class Custom_Model(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)




    def __str__(self):
        return self.name