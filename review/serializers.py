from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers

from .models import Review


class ReviewCreateSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    product_id = serializers.IntegerField(required=True)
    rating_score = serializers.FloatField(required=True, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    class Meta:
        model = Review
        fields = ('username', 'rating_score', 'body', 'created_at', 'product_id')

    def create(self, validated_data):
        review = Review.objects.create(**validated_data)
        return review


class ReviewDetailSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = ('username', 'rating_score', 'body', 'created_at')
