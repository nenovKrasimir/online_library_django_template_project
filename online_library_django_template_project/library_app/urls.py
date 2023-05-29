from django.urls import path, include

from online_library_django_template_project.library_app import views


urlpatterns = [
    path('add/', views.add_book, name='add-book'),
    path('details/<int:pk>', views.details_book, name='details-book'),
    path('edit/<int:pk>', views.edit_book, name='edit-book'),
    path('delete/<int:pk>', views.delete_book, name='delete-book')
]