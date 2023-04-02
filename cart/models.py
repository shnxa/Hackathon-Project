from django.db import models
from django.contrib.auth import get_user_model

from product.models import Product

User = get_user_model()
# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.product}: {self.quantity}'



