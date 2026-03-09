from django.db import models
from django.contrib.auth.models import AbstractUser
 
# Create your models here.


class Furniture_Details(models.Model):
    class CategoryChoices(models.TextChoices):
        living_spaces = "Living Spaces"
        bedrooms = "Bedrooms"
        kitchen = "Kitchen"
        bathrooms = "Bathrooms"

    src = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50,
        choices=CategoryChoices.choices
    )

    def __str__(self):
        return self.title

