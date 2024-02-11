from django.db import models
from django.contrib.auth.models import User

class Sneaker(models.Model):
    name = models.CharField(max_length=10)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    size = models.DecimalField(max_digits=3, decimal_places=1, default=35.0, choices=[(i / 2, str(i / 2)) for i in range(70, 91)])
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_in_stock = models.IntegerField()

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Stock(models.Model):
    sneaker = models.OneToOneField(Sneaker, on_delete=models.CASCADE)
    remaining_quantity = models.IntegerField()
