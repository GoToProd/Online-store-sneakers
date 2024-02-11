from django.contrib import admin
from .models import Sneaker, Basket

@admin.register(Sneaker)
class SneakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'color', 'size', 'price', 'quantity_in_stock']

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['user', 'sneaker', 'quantity']
