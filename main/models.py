from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import models
from django.views.generic import CreateView, UpdateView, DeleteView


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='projects')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Feedback(models.Model):
    name = models.CharField('Name', max_length=20)
    email = models.EmailField()
    message = models.TextField('Message')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


class CreatePortfolioView(PermissionRequiredMixin, CreateView):
    permission_required = 'main.add_portfolio'
    model = Portfolio
    fields = ('title', 'description', 'image', 'url')


class DeletePortfolioView(PermissionRequiredMixin, DeleteView):
    permission_required = 'main.delete_portfolio'
    model = Portfolio
    fields = ('title', 'description', 'image', 'url')
