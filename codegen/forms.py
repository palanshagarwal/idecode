from .models import Snippet
from django import forms
from django_ace import AceWidget


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['text', 'lang', 'file_name']
        widgets = {
            "text": AceWidget(mode='python', theme='twilight', width="700px", height="600px"),
        }