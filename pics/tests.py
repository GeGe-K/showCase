from django.test import TestCase
from .models import Category,Photo

# Create your tests here.
class PhotoTestClass(TestCase):

    # Set up method 
    def setUp(self):
        
        self.category = Category(name = 'Metal Box')
        self.category.save_category()
        self.photo = Photo(photo='photo.jpg', name = 'photo', description = 'testing photo', category = self.category)

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.photo, Photo))

    # Testing save method
    def test_save_method(self):
        self.photo.save_photo()
        photo = Photo.objects.all()
        self.assertTrue(len(photo)>0)

    # Testing delete method
    def test_delete_method(self):
        self.photo.save_photo()
        self.photo.delete_photo()


class CategoryTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.category = Category(name='Sports')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    # Testing save method
    def test_save_method(self):

        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    # Testing delete method
    def test_delete_method(self):

        self.category.save_category()
        self.category.delete_category()
