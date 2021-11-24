from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_reviews, name='reviews'),
    path('create/', views.create_review, name='create_review'),
    path('<int:pk>/delete', views.ReviewDeleteView.as_view(), name='reviews-delete')
]
