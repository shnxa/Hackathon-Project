from django.db import models

from product.models import Product


# Create your models here.


class Review(models.Model):
    user = models.ForeignKey('auth.User', related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} --> {self.product}'