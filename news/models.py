from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import models
from django.views.generic import CreateView, DeleteView, UpdateView


class Articles(models.Model):
    title = models.CharField('Title', max_length=50)
    full_text = models.TextField('Text')
    article_img = models.ImageField(upload_to='images/', null=True, blank=True)
    date = models.DateTimeField('Date published')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'


class CreatePostView(PermissionRequiredMixin, CreateView):
    permission_required = 'news.add_articles'
    model = Articles
    fields = ('title', 'full_text', 'article_img', 'date')


class UpdatePostView(PermissionRequiredMixin, UpdateView):
    permission_required = 'news.change_articles'
    model = Articles


class DeletePostView(PermissionRequiredMixin, DeleteView):
    permission_required = 'news.delete_articles'
    model = Articles
    fields = ('title', 'full_text', 'article_img', 'date')
