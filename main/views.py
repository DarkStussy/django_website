from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import FeedbackForm


def index(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


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
