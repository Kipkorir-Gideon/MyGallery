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

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_save_method(self):
        self.image.save_image()
        image = Image.objects.all()      
        self.assertTrue(len(image) >0)

    def test_delete_image(self):
        self.image.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image)== 0)

    def test_update_image(self):
        self.image.save_image()
        self.image.update_image(self.image.id, 'images/gidz.jpg')
        changed_img = Image.objects.filter(image='images/gidz.jpg')
        self.assertTrue(len(changed_img) > 0)


class CategoryTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.category = Category(category_name="Favorite")
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_method(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.category.save_category()
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

    def test_update_category(self):
        self.category.save_category()
        self.category.update_category(self.category.id, 'Food')
        changed_category = Category.objects.filter(name ='Food')
        self.assertTrue(len(changed_category) > 0)



class LocationTestClass(TestCase):

    def setUp(self):
        self.location = Location(location_name = 'Karatina')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))
        
    def test_save_method(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location)== 0) 
       
    def test_update_location(self):
        self.location.save_location()
        self.location.update_location(self.location.id, 'Karatina')
        changed_location = Location.objects.filter(name ='Karatina')
        self.assertTrue(len(changed_location) > 0) 