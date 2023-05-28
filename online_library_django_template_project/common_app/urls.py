from django.urls import path, include

from online_library_django_template_project.common_app import views


urlpatterns = [
    path('', views.home_page, name='home-page'),
]