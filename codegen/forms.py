from .models import Snippet
from django import forms
from django_ace import AceWidget


class SnippetForm(forms.ModelForm):
    write_key = forms.CharField(required=False)
    class Meta:
        model = Snippet
        fields = ['text', 'lang', 'file_name']
        widgets = {
            "text": AceWidget( theme='twilight', width="700px", height="600px"),
        }