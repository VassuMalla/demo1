from django.db import models

# Create your models here.

class PlacedModel(models.Model):
    NAME=models.CharField(max_length=50)
    STREAM=models.CharField(max_length=50)
    YEAR=models.DateField(auto_now=False, auto_now_add=False)
