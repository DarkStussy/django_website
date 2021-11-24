from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views.generic import DetailView, DeleteView, UpdateView

from .models import Articles, UpdatePostView, DeletePostView
from django.contrib.auth.decorators import permission_required
from .forms import ArticlesForm


def home_news(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/home_news.html', {'news': news})


@permission_required('news.add_articles', raise_exception=True)
def create(request):
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_news')
        else:
            messages.error(request, 'Error. Form isn\'t valid')

    form = ArticlesForm()

    data = {
        'form': form
    }

    if not request.user.has_perm('news.add_articles'):
        raise PermissionDenied
    else:
        return render(request, 'news/create.html', data)


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdatePostView, UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


class NewsDeleteView(DeletePostView, DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'news/news-delete.html'
    context_object_name = 'article'
