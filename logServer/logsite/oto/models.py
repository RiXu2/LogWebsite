from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField('Name', max_length=11)


class Country(models.Model):
    name = models.CharField('Country', max_length=20)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
