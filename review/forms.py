from django.forms import ModelForm, Textarea, CharField, HiddenInput, DateTimeField

from .models import Reviews


class ReviewsForm(ModelForm):
    name = CharField(max_length=20, widget=HiddenInput())

    class Meta:
        model = Reviews
        fields = ['name', 'text']

        widgets = {
            "text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Text"
            })
        }
