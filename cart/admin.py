from django.contrib import admin
from .models import *

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    fields = ['user','product','quantity','is_paid','paid_time']
    list_display=('id','get_products')

    def get_products(self, obj):
        return "\n-".join([p.name for p in obj.product.all()])
    


admin.site.register(User)  
admin.site.register(Product)  
admin.site.register(Cart,CartAdmin)    

