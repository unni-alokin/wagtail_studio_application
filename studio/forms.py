from django.forms import ModelForm
from django import forms
from studio.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:

        model = Contact

        fields = ('Name', 'Email', 'Subject', 'Message')