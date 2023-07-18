from django.test import TestCase
from django.urls import reverse

from  product.models import ProductVaraiant , Colour, Size , Brand , Product

# Create your tests here.
#
#
# class TestCart(TestCase):
#
#
#
#     def test_detail_cart_by_name(self):
#         response = self.client.get(reverse('cart:detail_cart'))
#         return self.assertEqual(response.status_code , 200)


    # def test_add_to_cart_by_name(self):
    #     response = self.client.get(reverse('cart:add_to_cart'), args = [1])
    #     self.assertEqual(response.status_code , 200 )
