from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views.generic import DeleteView, DetailView

from .forms import FeedbackForm, PortfolioForm
from .models import Portfolio, DeletePortfolioView


def index(request):
    return render(request, 'main/home.html')


def projects(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'main/projects.html', {"projects": portfolio})


@permission_required('main.add_portfolio', raise_exception=True)
def add_project(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('about')
        else:
            messages.error(request, 'Error. Form isn\'t valid')
    else:
        form = PortfolioForm()

    if not request.user.has_perm('main.add_portfolio'):
        raise PermissionDenied
    else:
        return render(request, 'main/add_project.html', {'form': form})


class DetailProjectView(DetailView):
    model = Portfolio
    template_name = 'main/project_detail.html'
    context_object_name = 'project'


class DeleteProjectView(DeletePortfolioView, DeleteView):
    model = Portfolio
    success_url = '/about'
    template_name = 'main/project_delete.html'
    context_object_name = 'project'


def feedback_show(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The message has been sent')
            return redirect('index')
        else:
            messages.error(request, 'Unable to complete request')

    form = FeedbackForm()

    return render(request, 'main/feedback.html', {'form': form})
