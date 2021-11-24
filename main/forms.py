from django.forms import ModelForm, TextInput, DateTimeInput, EmailInput, Textarea

from main.models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']

    widgets = {
        "Name": TextInput(attrs={
            "class": "form-control",
            "placeholder": "Name",

        }),
        "date": EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Email"
        }),
        "message": Textarea(attrs={
            "class": "form-control",
            "placeholder": "Message"
        })
    }