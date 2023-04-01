from rest_framework import serializers
from cart.models import Cart



class OrderSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='Cart.product')
    quantity = serializers.ReadOnlyField(source='Cart.ordered_quantity')
    price = serializers.ReadOnlyField(source='Product.price')

    class Meta:
        model = Cart
        fields = "__all__"

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['Product\'s title'] = instance.title
        repr['Product\'s price per one'] = instance.price
        repr['Your total'] = (instance.title * instance.price)
        return repr



