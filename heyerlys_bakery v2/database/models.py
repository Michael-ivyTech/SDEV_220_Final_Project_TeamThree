from django.db import models
from django.utils import timezone


# MenuItem can be used for a generalized menu structure
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ${self.price}"


# BakedGood stores items for orders
class BakedGood(models.Model):
    item_name = models.CharField(max_length=100)
    item_cost = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.item_name} (${self.item_cost})"


# Customer information
class Customer(models.Model):
    user = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.user}"


# Orders
class OrderInfo(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    baked_goods = models.ManyToManyField(BakedGood, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def get_total_cost(self):
        total = 0
        for item in self.orderitem_set.all():
            total += item.bakedgood.item_cost * item.quantity
        return total

    def __str__(self):
        return f"Order #{self.id} - {self.customer}"


class OrderItem(models.Model):
    orderinfo = models.ForeignKey(OrderInfo, on_delete=models.CASCADE)
    bakedgood = models.ForeignKey(BakedGood, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} × {self.bakedgood.item_name}"
