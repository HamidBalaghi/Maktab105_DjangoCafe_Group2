from django.contrib.auth.models import User
from django.db import models
from menu.models import Product, Table


# Create your models here.

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)

    # class Meta:
    #     unique_together = ("order", "menu")


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    paid_time = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return f"ID: {self.id} | User: {self.user}"


class ReserveTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    is_reserved = models.BooleanField(default=False)
    reserved_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    repay_time = models.DateTimeField(null=True, blank=True, auto_now=True)

