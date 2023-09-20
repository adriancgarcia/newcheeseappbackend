from django.db import models

# Create your models here.
class Cheese(models.Model):
    typeofcheese = models.CharField(max_length=200)
    countryoforigin = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
