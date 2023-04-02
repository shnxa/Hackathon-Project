from itertools import count

from django.db.models import Sum
from rest_framework import serializers
from cart.models import Cart
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from product.models import Product
from product.serializers import ProductListSerializer

User = get_user_model()

class OrderCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")
    username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Cart
        fields = "__all__"

    def validate(self, attrs):
        request = self.context['request']
        user = request.user
        product = attrs['product']
        quantity = attrs['quantity']
        return attrs

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['Added to cart:'] = instance.product.title
        return repr

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('quantity',)

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['products: '] = instance.product.title
        repr['total: '] = instance.product.price * instance.quantity
        user = self.context
        return repr
#
class OrderRemoveSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")
    username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Cart
        fields = "__all__"

    def validate(self, attrs):
        request = self.context['request']
        user = request.user
        product = attrs['product']
        quantity = attrs['quantity']
        return attrs

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['Deleted from cart:'] = instance.product.title
        return repr
#
#
#
#
