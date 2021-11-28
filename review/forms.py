from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, ModelChoiceField, HiddenInput
from .models import Reviews


class ReviewsForm(ModelForm):
    author = ModelChoiceField(queryset=User.objects.all(), widget=HiddenInput())

    class Meta:
        model = Reviews
        fields = ['author', 'text']

        widgets = {
            "text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Text"
            })
        }
