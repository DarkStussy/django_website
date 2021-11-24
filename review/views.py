from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DeleteView

from .forms import ReviewsForm
from .models import Reviews, DeleteReviewView


def show_reviews(request):
    reviews = Reviews.objects.order_by('-date')
    return render(request, 'reviews/show_reviews.html', {'reviews': reviews})


@login_required
def create_review(request):
    if request.method == "POST":
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
        else:
            messages.error('Error. Form isn\'t valid')

    form = ReviewsForm(initial={'name': request.user.username})

    data = {
        'form': form
    }

    return render(request, 'reviews/create_review.html', data)


class ReviewDeleteView(DeleteReviewView, DeleteView):
    model = Reviews
    success_url = '/reviews'
    template_name = 'reviews/reviews-delete.html'
    context_object_name = 'review'
