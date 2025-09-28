from django.db import models

# Create your models here.

# Book model represents a published book.
# - title: the book's title
# - publication_year: the year the book was published
# - author: foreign key linking each book to a single Author.
#   (One Author -> Many Books)
#   related_name='author_related_name' allows reverse access:
#   author.author_related_name.all() gives all books for that author.

class Author(models.Model):
    name = models.CharField(max_length=30)

class Book(models.Model):
    title = models.CharField()
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_related_name')