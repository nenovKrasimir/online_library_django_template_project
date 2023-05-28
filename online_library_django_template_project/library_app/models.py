from django.db import models

from online_library_django_template_project.profile_app.models import UserProfile


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/')
    type = models.CharField(max_length=30)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f'{self.title} of type {self.type}'