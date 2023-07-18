from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ContactUs(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField()

    def __str__(self):
        return f'{self.user} : {self.username}'