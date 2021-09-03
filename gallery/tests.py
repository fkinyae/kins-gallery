from django.test import TestCase
from .models import Location,Category,Image

class CategoryTestClass(TestCase):
    def setUp(self):
        self.francis = Category(category='Adventure')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.francis,Category))   
        
    def test_save_method(self):
        self.francis.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)     
        
class LocationTestClass(TestCase):
    def setUp(self):
        self.kinyae = Location(location='Nakuru')     
        
    def test_instance(self):
        self.assertTrue(isinstance(self.kinyae,Location))
        
    def test_save_method(self):
        self.kinyae.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)        
        
class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(location='Nairobi')
        self.location.save_location()

        self.category = Category(category='love')
        self.category.save_category()
        
        self.mumo = Image(id=1,photo_image='kin.jpg',image_name='test',image_description='test image',location_id=self.location,category_id=self.category,date_posted='2021-04-12')   
        
    def test_instance(self):
        self.assertTrue(isinstance(self.mumo,Image))        
        
    def test_save_method(self):
        self.mumo.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)    
        
    def test_delete_image(self):
        self.mumo.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image)==0)         
        
