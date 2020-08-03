from django.core.exceptions import ValidationError
from django.forms import HiddenInput
from django.forms.models import ModelForm
from django import forms
from .models import ContactUs
from .models import Questionnaire


class ContactUsForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'message']