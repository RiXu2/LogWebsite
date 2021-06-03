from django.contrib import admin
from .models import Log

# Register your models here.


class LogManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'info']
    list_display_links = ['title']
    list_filter = ['title']
    #模糊查询
    search_fields = ['title', 'info']
    #添加可在列表页编辑的字段
    #list_editable = ['info']


admin.site.register(Log, LogManager)
