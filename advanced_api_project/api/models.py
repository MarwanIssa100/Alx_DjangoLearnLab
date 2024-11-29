from django.db import models

# Create your models here.

class Author(models.Model):
    """
    Author model to handel authors table in database
    """
    name = models.CharField(max_length=100)
    
    
class Book(models.Model):
    """
    Book model to handel books table in database
    """
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()