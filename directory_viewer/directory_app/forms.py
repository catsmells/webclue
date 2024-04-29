from django import forms
from .models import Website

class URLForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['url']
