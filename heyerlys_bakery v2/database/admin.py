# database/admin.py
from django.contrib import admin
from .models import Customer, BakedGood, OrderInfo

admin.site.register(Customer)
admin.site.register(BakedGood)
admin.site.register(OrderInfo)
