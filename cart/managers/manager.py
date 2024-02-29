
from django.db import models
from cart.models import Cart


class CartManager(models.Manager):
    def get(self):
        object=Cart.objects.filter(is_paid=False)
        return object
    