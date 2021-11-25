from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

from news.models import Articles


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'full_text', 'article_img', 'date']

        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Title",

            }),
            "date": DateTimeInput(attrs={
                "class": "form-control",
                "placeholder": "Date published"
            }),
            "full_text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Text"
            })
        }
