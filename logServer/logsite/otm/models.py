from django.db import models

# Create your models here.


class Editor(models.Model):
    name = models.CharField('Name', max_length=50)


class Log(models.Model):
    title = models.CharField('title', max_length=11)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
