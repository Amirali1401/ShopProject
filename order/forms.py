from django import forms

from .models import Order , OrderChoice

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('first_name' , 'last_name' , 'email' ,'phone_number',  'address')



class OrderwayForm(forms.ModelForm):

    class Meta:
        model = OrderChoice
        fields = ('choice_order',)