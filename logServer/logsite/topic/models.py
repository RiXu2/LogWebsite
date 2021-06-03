from django.db import models

# Create your models here.


class Topic(models.Model):

    title = models.CharField(max_length=50, verbose_name='Log Name')
    category = models.CharField(max_length=20, verbose_name='Log Type')
    limit = models.CharField(max_length=20, verbose_name='Log 权限')
    introduce = models.CharField(max_length=20, verbose_name='Log introduction')
    content = models.TextField(verbose_name='Log Content')
    created_time = models.DateTimeField(auto_now_add=True)
    Updated_time = models.DateTimeField(auto_now=True)
