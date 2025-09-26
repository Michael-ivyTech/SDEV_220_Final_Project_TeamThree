from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    order_id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return f"{self.order_id} {self.last_name} {self.first_name}"


class OrderInfo(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    order_cost = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.customer} {self.order_date} {self.order_cost}"
    
class BakedGood(models.Model):
    item_cost = models.DecimalField(max_digits=6, decimal_places=2)
    calories = models.IntegerField()

    def __str__(self):
        return f"{self.item_cost} {self.calories}"


#mysite = Bakery
#application = database
