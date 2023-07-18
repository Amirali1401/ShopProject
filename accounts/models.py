from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class ChangePassword(models.Model):
    old_password = models.CharField(max_length=200)
    new_password = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.new_password} + {self.old_password}'