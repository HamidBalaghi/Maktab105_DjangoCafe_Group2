from django.db import models


# Create your models here.
class Category(models.Model):
    pass


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name="products")

    def __str__(self):
        return self.name


class OrderProduct(models.Model):  # TODO: Creat app and move
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    class Meta:
        unique_together = ("order", "product")
