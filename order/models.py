from django.db import models
from django.contrib.auth.models import User

from product.models import Product


# Create your models here.


class OrderChoice(models.Model):
    WAY_CHOICES = (
        ('پست سفارشی تحویل یک روزه با قیمت 100000', 1),
        ('پست عادی تحویل 3-7 روزه با قیمت 20000', 2),
        ('پیک تحویل 5-8 روزه با قیمت 30000', 3),
    )

    choice_order = models.CharField(max_length=50, choices=WAY_CHOICES)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    address = models.TextField()
    zarinpal_authority = models.CharField(max_length=255)
    zarinpal_ref_id = models.CharField(max_length=155 , blank=True)
    zarinpal_data = models.TextField(blank=True)
    is_paid = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_total_sum(self):
        return sum(item.price * item.quantity for item in self.order_items)

    def __str__(self):
        return f'{self.id} : {self.first_name} : {self.last_name}'




class OrderItem(models.Model):
      order = models.ForeignKey(Order , on_delete = models.CASCADE , related_name='order_items')
      product = models.ForeignKey(Product , on_delete=models.CASCADE)
      price = models.PositiveIntegerField(default=0)
      quantity = models.PositiveIntegerField(default=1)

      date_created = models.DateTimeField(auto_now_add=True)
      date_modified = models.DateTimeField(auto_now=True)

      def __str__(self):
          return f'{self.order} : {self.quantity}'
