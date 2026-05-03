from django.urls import path
from . import views

urlpatterns = [
    #    path("", views.home),
    path("trigger-task/", views.trigger_task),
]
