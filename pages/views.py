from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import ContactUs
from .forms import ContactUsForm

# Create your views here.


class WelcomePage(generic.TemplateView):
    template_name = 'pages/welcome.html'



@login_required()
def contactus_view(request):
    form = ContactUsForm(request.POST)

    if form.is_valid():
        form_obj = form.save(commit=False)
        form_obj.user = request.user
        form_obj.save()

    return render(request , 'pages/contactus.html' , context={'form':form})