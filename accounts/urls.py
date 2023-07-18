from django.urls import path

from . import views as accounts_views

urlpatterns = [
   path('register/' , accounts_views.Register.as_view() , name = 'register'),
   path('change_account/' , accounts_views.change_account_user , name = 'change_account'),
   path('change_password/' , accounts_views.password_change_view , name = 'change_password'),

   ]