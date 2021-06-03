from django.db import models


# Create your models here.
class Log(models.Model):
    title = models.CharField('LogName', max_length=50, default='')
    sender_name = models.CharField('SenderName', max_length=50, default='')
    info = models.CharField('Info', max_length=100, default='')
    is_active = models.BooleanField('Delete', default=True)

    class Meta:
        db_table = 'log'

    def __str__(self):
        return '%s: %s %s' % (self.title, self.sender_name, self.info)


class User(models.Model):
    name = models.CharField('Name', max_length=50, default='')
    email = models.EmailField('Email')

    class Meta:
        db_table = 'user'
