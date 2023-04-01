from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')


    def __str__(self):
        return f'{self.product}'


