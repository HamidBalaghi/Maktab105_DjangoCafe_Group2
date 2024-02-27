from re import T
from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    name = models.CharField(max_length=255, default=None)
    description = models.TextField(default=None)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    number_of_products = models.IntegerField(default=0)


    def __str__(self):
        return self.name
    


# class ProductModel(models.Model):
#     category = models.ManyToManyField(CategoryModel)
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     image = models.ImageField(upload_to='images_pruducts/',blank=True,null=True)
#     price = models.DecimalField(max_digits=5,decimal_places=2)


#     def __str__(self):
#         return self.name