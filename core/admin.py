from django.contrib import admin
from .models import OrderItem, Order, Item, Timer


admin.site.register(OrderItem)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Timer)
