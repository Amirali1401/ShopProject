from django.urls import path

from . import views as pages_views

app_name = 'pages'

urlpatterns = [
    path('welcome' , pages_views.WelcomePage.as_view() , name = 'welcome'),
    path('contactus/' , pages_views.contactus_view , name = 'contactus'),
    ]