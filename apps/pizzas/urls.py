from django.urls import path

from apps.pizzas import views

app_name = 'apps.pizzas'
urlpatterns = [
    path('', views.index, name='index'),
]
