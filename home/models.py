from django.db import models


class Category(models.Model):  # TODO:delete this app
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/')
    sub_of = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
