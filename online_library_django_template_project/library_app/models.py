from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField
    image = models.ImageField(upload_to='images/')
    type = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.title} of type {self.type}'