from rest_framework import serializers

from category.models import Category
from product.serializers import ProductListSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['products_count'] = instance.products.count()
        repr['products'] = ProductListSerializer(instance=instance.products.all(), many=True).data
        return repr


