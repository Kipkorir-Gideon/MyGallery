from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=30)
    descrption = models.CharField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id ,name,description , location, category):
        update = cls.objects.filter(id = id).update(name = name,description=description,location= location,category=category)
        return update

    @classmethod
    def get_image_by_id(cls,id):
        image_id = cls.objects.filter(id = id).all()
        return image_id

    @classmethod
    def search_image(cls,category):
        images = Image.objects.filter(category__name__contains=category)
        return images

    @classmethod
    def filter_by_location(cls,location):
        image_location = cls.objects.filter(location=location).all()
        return image_location


    def __str__(self):
        return self.image



class Category(models.Model):
    category_name = models.CharField()



class Location(models.Model):
    location_name = models.CharField(max_length=30)
