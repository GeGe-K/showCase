from django.db import models
import datetime as dt

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Photo(models.Model):
    photo_path = models.ImageField(upload_to='photos/')
    name = models.CharField(max_length=40)
    description = models.TextField()
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()

    @classmethod
    def get_all_photos(cls):
        photos = cls.objects.order_by()
        return photos

    @classmethod
    def get_photo(cls, id):
        photo = cls.objects.get(id=id)
        return photo

    @classmethod
    def filter_by_category(cls, id):
        photos = cls.objects.filter(category_id=id)
        return photos

    @classmethod
    def search_photo(cls, category):
        photos = cls.objects.filter(category__name__icontains=category)
        return photos



