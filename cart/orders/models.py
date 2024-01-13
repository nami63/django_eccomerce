from django.db import models
from customers.models import Customer
from products.models import Product

class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE = ((LIVE, 'live'), (DELETE, 'Delete'))
    CART_STAGE = 1
    ORDER_CONFIRMED = 1
    ORDER_REJECTED = 4
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    STATUS_CHOICES = (
        (ORDER_PROCESSED, "ORDER_PROCESSED"),
        (ORDER_DELIVERED, "ORDER_DELIVERED"),
        (ORDER_REJECTED, "ORDER_REJECTED"),
    )
    order_status = models.IntegerField(choices=STATUS_CHOICES, default=CART_STAGE)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='orders')

    delete_status = models.DateTimeField(auto_now_add=True)
    create_status = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderedItem(models.Model):
    product = models.ForeignKey(Product, related_name='added_cards', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added_products')
