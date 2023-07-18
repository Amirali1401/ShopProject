from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.


class TestAccount(TestCase):

    def test_login_url_by_name(self):
        response = self.client.get(reverse('login'))
        return  self.assertEqual(response.status_code , 200)


    def test_register_url_by_name(self):
        response = self.client.get(reverse('register'))
        return self.assertEqual(response.status_code, 200)