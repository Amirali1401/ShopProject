from django.urls import path

from . import views as cart_views

app_name = 'cart'
urlpatterns = [
   path('' , cart_views.detail_cart_view , name ='detail_cart'),
   path('<int:product_id>/add_to_cart/' , cart_views.add_cart_view , name ='add_to_cart'),
   path('<int:product_id>/delete_form_cart/' ,cart_views.delete_from_cart , name = 'delete_from_cart' ),
   path('clear_cart/' , cart_views.clear_cart , name = 'clear_cart'),
   ]