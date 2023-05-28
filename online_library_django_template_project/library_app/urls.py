from django.urls import path, include

from online_library_django_template_project.library_app import views


urlpatterns = [
    path('add/', views.add_book, name='add-book'),
]