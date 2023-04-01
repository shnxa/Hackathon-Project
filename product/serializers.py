from rest_framework import serializers
from django.db.models import Avg


from category.models import Category
from product.models import Product, ProductImages
from review.serializers import ReviewSerializer



class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'author', 'book_cover', 'category', 'price', 'id')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['reviews_count'] = instance.reviews.count()
        repr['average rating for this product'] = instance.reviews.aggregate(Avg('rating_score'))['rating_score__avg']
        return repr

class ProductDetailSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(required=True, queryset=Product.objects.all())
    class Meta:
        model = Product
        fields = ('title', 'id', 'category', 'author', 'book_cover', 'price', 'quantity')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['average rating for this product'] = instance.reviews.aggregate(Avg('rating_score'))['rating_score__avg']
        repr['reviews_count'] = instance.reviews.count()
        repr['reviews'] = ReviewSerializer(instance=instance.reviews.all(), many=True).data
        user = self.context['request'].user
        return repr


class ProductCreateSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(required=True, queryset=Product.objects.all())
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())
    book_cover = ProductImagesSerializer(many=True, required=False)
    class Meta:
        model = Product
        fields = ('title', 'annotation', 'author', 'category', 'book_cover', 'price', 'quantity')

    def create(self, validated_data):
        request = self.context.get('request')
        product = Product.objects.create(**validated_data)
        images_data = request.FILES.getlist('images')
        for image in images_data:
            ProductImages.objects.create(book_cover=image, product=product)
        return product


