from django import forms

class AddToProductCart(forms.Form):
    QUANTITY_CHOICE = [(str(i) , i) for i in range(1,31)]

    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICE , coerce=int)
    inplace = forms.BooleanField(required=False , widget=forms.HiddenInput)