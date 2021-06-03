from django.urls import path

from . import views

urlpatterns = [
    path('all_log', views.all_log),
    path('update_log/<int:log_id>', views.update_log),
    path('delete_log', views.delete_log)
]