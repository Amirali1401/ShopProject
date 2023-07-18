from django.urls import path

from . import views as product_views

app_name = 'product'

urlpatterns = [
   #products url and comment url()
   path('' , product_views.index , name = 'index'),
   path('<int:product_id>/detail_products/' , product_views.detail_products_views , name = 'detail_products'),
   path('<int:category_id>/' , product_views.products_category , name = 'products_category'),
   path('<int:shop_id>/shops/' , product_views.shop_view , name = 'shop_view'),
   path('create_comment/' , product_views.CreateCommentView.as_view() , name = 'create_comment'),

   #wishlist_urls
   path('wishlist/' , product_views.wishlist_views , name = 'wishlist_products'),
   path('<int:product_id>/add_to_wishlist/' , product_views.add_to_wishlist , name = 'add_to_wishlist'),
   path('<int:product_id>/delete_from_wishlist/' , product_views.delete_from_wishlist , name = 'delete_from_wishlist'),

   #notification
   path('notification/' , product_views.ListViewNotifications.as_view() , name = 'list_notifications'),

   #search book
   path('search_result/' , product_views.SearchResultList.as_view() , name = 'search_books'),

   ]