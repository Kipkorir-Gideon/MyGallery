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
        self.location.update_location(self.location.id, 'Karen')
        changed_location = Location.objects.filter(name ='Karen')
        self.assertTrue(len(changed_location) > 0) 