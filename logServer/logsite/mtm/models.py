from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField('name', max_length=11)


class Log(models.Model):
    title = models.CharField('title', max_length=30)
    author = models.ManyToManyField(Author)