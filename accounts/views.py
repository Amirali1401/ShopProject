from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

from .forms import UserForm , PasswordChangeForm
from .models import ChangePassword



class Register(generic.CreateView):
    form_class = UserCreationForm                         # register view
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('pages:welcome')



@login_required()
def change_account_user(request):
    form = UserForm(instance=request.user , data = request.POST)
    password_form = PasswordChangeForm(user = request.user , data  = request.POST)
    if form.is_valid() and password_form.is_valid():                             #change user info
        form.save()
        password_form.save()

    return render(request, 'accounts/settings_accounts.html', context={'form': form , 'password_form':password_form})


@login_required()
def password_change_view(request):
    user_1 = request.user
    form = PasswordChangeForm(request.POST)
    if form.is_valid():

        if form.cleaned_data['old_password'] == user_1.password:
            user_1.password = form.cleaned_data['new_password']

        form.save()


    return render(request  , 'accounts/password_change_form.html' , context={'form':form})
