from django.forms import ModelForm, TextInput, Textarea, CharField, EmailField
from django import forms

from .models import Feedback
from .models import Portfolio


class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'field', 'description', 'image', 'url']

    widgets = {
        "title": TextInput(attrs={
            "class": "form-control",
            "placeholder": "Title"

        }),
        "field": TextInput(attrs={
            "class": "form-control",
            "placeholder": "Field"

        }),
        "description": Textarea(attrs={
            "class": "form-control",
            "placeholder": "Description"
        })
    }


class FeedbackForm(ModelForm):
    name = CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    email = EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    message = CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control'}))

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
