from django.urls import path

from apps.meal_plans import views

app_name = 'apps.meal_plans'
urlpatterns = [
    path('', views.index, name='index'),
]
