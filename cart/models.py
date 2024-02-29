from enum import auto
from os import name
from tkinter import N
from django.db import models

# Create your models here.



class User(models.Model):
    name=models.CharField(max_length=255,default=None)
    
    def __str__(self):
        return self.name
       
    


class Product(models.Model):
    name=models.CharField(max_length=255,default=None)


    def __str__(self):
        return self.name


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ManyToManyField(Product)
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_paid=models.BooleanField(default=False)
    paid_time=models.DateTimeField(null=True,blank=True) 



    # def __str__(self):
    #     return self.user  
