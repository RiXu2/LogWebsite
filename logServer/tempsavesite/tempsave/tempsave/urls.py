"""tempsave URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', views.all_content),
    path('admin/', admin.site.urls),
    path('test_cache', views.test_cache),
    path('test_mw', views.test_mw),
    path('test_csrf', views.test_csrf),
    path('test_page', views.test_page),
    path('test_csv', views.test_csv),
    path('make_page_csv', views.make_page_csv),
    path('test_upload', views.test_upload),
    path('all_content', views.all_content),
    path('delete_content', views.delete_content),
    path('update_content/<int:content_id>', views.update_content),
    re_path(r'^download/(?P<file_path>.*)/$', views.file_response_download, name='file_download'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
