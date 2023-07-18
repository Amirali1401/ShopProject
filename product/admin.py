from django.contrib import admin

from .models import Product , Shop , Category  , ProductVaraiant , Colour , Size , Brand , Comment , Notification
# Register your models here.



admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(ProductVaraiant)
admin.site.register(Colour)
admin.site.register(Size)
admin.site.register(Brand)
admin.site.register(Comment)
admin.site.register(Notification)
