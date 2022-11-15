from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.views import View
from django.views.generic import TemplateView

from studio.forms import ContactForm
from django import forms
from myproject.settings import emailtest

from myproject import templates

class ContactView(View):
   def post(self, request):
    form = ContactForm(request.POST)

    if form.is_valid():
        form.save()
        send_mail('django test mail', 'this is django test body',emailtest.EMAIL_HOST_USER,['unnikrishnank@alokin.in'], fail_silently=True)
        flag=1
        return render(request,'contact/contact_page.html', {'flag':flag})
    return render(request, 'contact/contact_page.html', {'form': form})

   def get(self, request):
    flag=0
    form = ContactForm()
    return render(request,'contact/contact_page.html', {'form': form,'flag':flag})
