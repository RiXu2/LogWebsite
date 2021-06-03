from django.db import models

# Create your models here.


class Content(models.Model):

    title = models.CharField('Title', max_length=50)
    picture = models.FileField(upload_to='file')
    Updated_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField('Delete', default=True)