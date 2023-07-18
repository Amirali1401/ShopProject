from django import forms
from django.contrib.auth.models import User

from .models import ChangePassword

# class RegisterForm(UserCreationForm):
#     class Meta:                                #register form
#         model = User
#         fields = ('username' , 'email' , 'password1' , 'password2')



class UserForm(forms.ModelForm):

    class Meta:                               #User Form
        model = User
        fields = ['username','email' ,'password']




class PasswordChangeForm(forms.ModelForm):

      class Meta:
          model = ChangePassword
          fields = "__all__"