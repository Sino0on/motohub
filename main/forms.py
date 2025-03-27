from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Application
