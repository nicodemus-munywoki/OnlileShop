from django.db import models

# Create your models here.

class Productss(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    dec = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)