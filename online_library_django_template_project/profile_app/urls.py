from django.urls import path, include

from online_library_django_template_project.profile_app import views


urlpatterns = [
    path('<int:pk>', views.ProfileDetailView.as_view(), name='details-profile'),
    path('edit/', views.ProfileEditView.as_view(), name='edit-profile'),
    path('delete/', views.ProfileDeleteView.as_view(), name='delete-profile')
]