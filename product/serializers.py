from rest_framework import serializers
from category.models import Category
from product.models import Product, ProductImages
from review.serializers import ReviewSerializer


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    product_title = serializers.ReadOnlyField(source='product.title')
    author_name = serializers.ReadOnlyField(source='product.author')
    class Meta:
        model = Product
        fields = ('author_name', 'category_name', 'product_title', 'book_cover')

    @staticmethod
    def is_favorite(product, user):
        return user.favorites.filter(product=product).exists()

    @staticmethod
    def is_in_cart(product, user):
        return user.cart.filter(product=product).exists()

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['reviews_count'] = instance.reviews.count()
        user = self.context['request'].user
        if user.is_authenticated:
            repr['is_favorite'] = self.is_favorite(instance, user)
            repr['is_in_cart'] = self.is_in_cart(instance, user)
        return repr

class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())
    images = ProductImagesSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"

    @staticmethod
    def is_favorite(product, user):
        return user.favorites.filter(product=product).exists()

    @staticmethod
    def is_in_cart(product, user):
        return user.cart.filter(product=product).exists()

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['reviews_count'] = instance.reviews.count()
        repr['reviews'] = ReviewSerializer(instance=instance.comments.all(), many=True).data
        user = self.context['request'].user
        if user.is_authenticated:
            repr['is_favorite'] = self.is_favorite(instance, user)
            repr['is_in_cart'] = self.is_in_cart(instance, user)
        return repr


class ProductCreateSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())
    images = ProductImagesSerializer(many=True, required=False)
    class Meta:
        model = Product
        fields = ('title', 'annotation', 'author', 'category', 'preview', 'book_cover')

    def create(self, validated_data):
        request = self.context.get('request')
        product = Product.objects.create(**validated_data)
        images_data = request.FILES.getlist('images')
        for image in images_data:
            ProductImages.objects.create(book_cover=image, product=product)
        return product