from django.test import TestCase
from .models import Image,Location,Category
import datetime as dt

# Create your tests here.
class ImageTestClass(TestCase):

    #Set up method 
    def setUp(self):
        #Posting a new image and saving it.
        self.image = Image(name='Image1', description='An image to test the posting method.', location= self.location, category= self.category)
        self.image.save()
