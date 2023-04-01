from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = ('username', 'rating_score', 'body', 'created_at')


