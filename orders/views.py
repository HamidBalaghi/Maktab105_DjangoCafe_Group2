from django.shortcuts import render
from django.views.generic import ListView, UpdateView

from orders.models import Order, OrderItem


# Create your views here.

class AllOrders(ListView):
    model = Order
    template_name = 'basket/allcarts.html'

    def get_queryset(self):
        return Order.objects.filter(is_paid=False)


class OrderDetail(UpdateView):
    model = Order
    fields = '__all__'
    template_name = 'basket/cart.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        result = (list(request.POST)[1])
        if 'payNow' in result:
            order = Order.objects.get(id=self.object.id)
            order.is_paid = True
            order.save()
        elif 'clearCart' in result:
            order = Order.objects.get(id=self.object.id)
            for item in order.order_items.all():
                item.delete()
        elif 'deleteItem_' in result:
            item_id = result.split('_')[1]
            item = OrderItem.objects.get(id=item_id)
            item.delete()
        elif 'decreaseQuantity_' in result:
            item_id = result.split('_')[1]
            item = OrderItem.objects.get(id=item_id)
            item.quantity -= 1
            item.save()
        elif 'increaseQuantity_' in result:
            item_id = result.split('_')[1]
            item = OrderItem.objects.get(id=item_id)
            item.quantity += 1
            item.save()

        return self.render_to_response(self.get_context_data())
