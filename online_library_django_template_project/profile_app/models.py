from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    MAX_NAME_LENGTH = 30

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=MAX_NAME_LENGTH)
    last_name = models.CharField(max_length=MAX_NAME_LENGTH)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

