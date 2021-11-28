from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.db import models
from django.views.generic import DeleteView


class Reviews(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField('Text', max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class DeleteReviewView(PermissionRequiredMixin, DeleteView):
    permission_required = 'reviews.delete_reviews'
    model = Reviews
    fields = ('text', 'date')


