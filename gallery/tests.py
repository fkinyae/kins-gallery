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
