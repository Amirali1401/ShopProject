from django import forms

from .models import ProductVaraiant , Product  ,Colour , Comment


class ProductForm(forms.ModelForm):

    class Meta:
        model = Colour
        fields = ('title',)



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text' , )