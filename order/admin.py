from django.contrib import admin

from .models import Order , OrderItem , OrderChoice
# Register your models here.


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderChoice)