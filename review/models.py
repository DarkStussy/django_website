from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import models
from django.views.generic import DeleteView


class Reviews(models.Model):
    name = models.CharField('Name', max_length=20)
    text = models.TextField('Text')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/reviews/{self.id}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class DeleteReviewView(PermissionRequiredMixin, DeleteView):
    permission_required = 'reviews.delete_reviews'
    model = Reviews
    fields = ('name', 'text', 'date')


