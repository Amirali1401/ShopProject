from django.test import TestCase
from django.urls import reverse

from .models import Order , OrderItem
# Create your tests here.



class OrderTest(TestCase):

    # def test_list_orders(self):
    #     response = self.client.get(reverse('order:list_orders'))
    #     return self.assertEqual(response.status_code , 200)


    def test_order_create_template_by_name(self):
         response = self.client.get(reverse('order:order_create'))
         return self.assertTemplateNotUsed(response , 'order/order_create.html')