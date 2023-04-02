from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()
# Create your models here.


class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating_score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], null=True,
                                     default=None)
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'product']
    def __str__(self):
        return f'User {self.user}\'s review on {self.product.title}'


