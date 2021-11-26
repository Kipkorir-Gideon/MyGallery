from django.db import models
import datetime as dt

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=30)
    descrption = models.CharField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to = 'gallery')



class Category(models.Model):
    name = models.CharField()