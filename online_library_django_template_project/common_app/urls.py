from django.urls import path, include

from online_library_django_template_project.common_app import views


urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('login/', views.login_page, name='login-page'),
    path('register/', views.register_page, name='register-page'),
    path('logout/', views.logout_page, name='logout')
]