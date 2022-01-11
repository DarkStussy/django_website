from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('addproject/', views.add_project, name='add_project'),
    path('<int:pk>', views.DetailProjectView.as_view(), name='project-detail'),
    path('<int:pk>/deleteproject', views.DeleteProjectView.as_view(), name='delete-project'),
    path('feedback/', views.feedback_show, name='feedback'),
]
