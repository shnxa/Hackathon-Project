from django.db import models

from category.models import Category


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    annotation = models.TextField(blank=True)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    book_cover = models.ImageField(upload_to='images/', null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.title} by {self.author}'


class ProductImages(models.Model):
    title = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    def generate_name(self):
        from random import randint
        return 'image' + str(self.id) + str(randint(100000, 1_000_000))

    def save(self, *args, **kwargs):
        self.title = self.generate_name()
        return super(ProductImages, self).save(*args, **kwargs)
