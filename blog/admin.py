from django.contrib import admin
from .models import (
    ContactUs,
    Questionnaire,
    Questionnaire35001,
    CompareReport
)

# Register your models here.

admin.site.register(ContactUs)
admin.site.register(Questionnaire)
admin.site.register(CompareReport)
admin.site.register(Questionnaire35001)
