from django.urls import path

from . import views as order_views

app_name = 'order'

urlpatterns = [
   path('orders/' , order_views.order_view , name = 'list_orders'),
   path('' , order_views.order_create_view , name = 'order_create'),
   path('checkout/' , order_views.checkout_view , name = 'checkout'),
   ]