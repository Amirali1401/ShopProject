from django.db import models
from django.contrib.auth.models import User

from datetime import date


# Create your models here.


class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateField(default=date.today)
    shop_name = models.CharField(max_length=255)

    # Shop Product models
    def __str__(self):
        return f'{self.id} : {self.shop_name}'



class Category(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name_cat = models.CharField(max_length = 255)
    slug = models.SlugField(max_length = 255)

    def __str__(self):
        return f'{self.name_cat} + {self.id}'


class Colour(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title



class Size(models.Model):
    title = models.CharField(max_length=100)
    size_code = models.CharField(max_length=50, null=True)


class Brand(models.Model):
    title = models.CharField(max_length=100)
    brand_code = models.CharField(max_length=50, null=True)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products_shop', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products_category')
    slug = models.SlugField(max_length = 255 , unique=True )
    regular_price = models.PositiveIntegerField(default=0)
    selling_price = models.PositiveIntegerField(default=0)
    color = models.ManyToManyField(to = Colour , related_name='products_color')
    covers = models.ImageField(upload_to='covers/')
    is_active = models.BooleanField(default=False)  # Product model

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f' {self.name}'


class ProductVaraiant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name='product_Varaiant_item')
    color = models.ForeignKey(Colour, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['product', 'color', 'size', 'brand'],
    #             name='unique_prod_color_size_combo',
    #         )
    #     ]


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'


#To store comments about product
class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    text = models.TextField()
    products = models.ForeignKey(Product , on_delete=models.CASCADE , related_name = 'comments')

    def __str__(self):
        return f'{self.user} : {self.text}'




class Notification(models.Model):
    unread = models.BooleanField(default=False)
    text = models.TextField()
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} : {self.text}'