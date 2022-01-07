from django.forms import ModelForm, TextInput, EmailInput, Textarea, URLField

from .models import Feedback
from .models import Portfolio


class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'description', 'image', 'url']

    widgets = {
        "title": TextInput(attrs={
            "class": "form-control",
            "placeholder": "Title",

        }),
        "description": Textarea(attrs={
            "class": "form-control",
            "placeholder": "Description"
        })
    }


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']

    widgets = {
        "Name": TextInput(attrs={
            "class": "form-control",
            "placeholder": "Name",

        }),
        "email": EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Email"
        }),
        "message": Textarea(attrs={
            "class": "form-control",
            "placeholder": "Message"
        })
    }
