from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('addproject/', views.add_project, name='add_project'),
    path('<int:pk>/deleteproject', views.DeleteProjectView.as_view(), name='delete-project'),
    path('feedback/', views.feedback_show, name='feedback'),
]
