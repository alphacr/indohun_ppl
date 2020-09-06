from django.core.exceptions import ValidationError
from django.forms import HiddenInput
from django.forms.models import ModelForm
from django import forms
from .models import ContactUs
from .models import Questionnaire
from .models import CompareReport



class ContactUsForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = ContactUs
        fields = ['nama_lengkap', 'email', 'alamat', 'pesan']

class CompareReportForm(forms.ModelForm):
    class Meta:
        model = CompareReport
        fields = ['pilihan_1', 'pilihan_2']