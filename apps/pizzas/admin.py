from django.contrib import admin
from apps.pizzas.models import Pizza, Topping


admin.site.register(Pizza)
admin.site.register(Topping)
