from django.contrib.auth.models import User
from django.db import models
from menu.models import Product, Table
from django.contrib.auth import get_user_model


# Create your models here.


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="order_items"
    )
    order = models.ForeignKey(
        "Order", on_delete=models.CASCADE, related_name="order_items"
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("order", "product")

    @property
    def total_price_item(self):
        return self.quantity * self.product.price


class PaidOrderManager(models.Manager):
    def get_queryset(self):
        user_model = get_user_model()
        if user_model.is_authenticated:
            return super().get_queryset().filter(is_paid=True)
        else:
            return super().get_queryset().none()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    paid_time = models.DateTimeField(null=True, blank=True, auto_now=True)
    paid_object = PaidOrderManager()

    @property
    def total_price(self):
        total = 0
        for item in self.order_items.all():
            total += item.total_price_item
        return total

    def __str__(self):
        return f"ID: {self.id} | User: {self.user}"


class ReserveTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    is_reserved = models.BooleanField(default=False)
    reserved_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    repay_time = models.DateTimeField(null=True, blank=True, auto_now=True)
