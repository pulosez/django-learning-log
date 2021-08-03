"""Defines URL patterns for learning_logs."""

from django.urls import path

from apps.learning_logs import views

app_name = 'apps.learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]