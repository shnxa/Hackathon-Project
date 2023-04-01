from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.decorators import action


from . import serializers


from cart.models import Cart
from product.serializers import ProductListSerializer

# Create your views here.
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @action(['DELETE'], detail=True)
    def perform_destroy(self, request):
        product = self.get_object()
        Cart.objects.delete(product=product)
        return Response('Successfully removed from your order cart!', status=200)

    @action(['GET'], detail=True)
    def list(self, request):
        cart = Cart.objects.all()
        serializer = ProductListSerializer(cart, many=True)
        return Response(serializer.data, status=200)

    @action(['PATCH'], detail=True)
    def partial_update(self, serializer):
        instance = self.get_object()
        self.request.data.get('quantity', None)
        updated_instance = serializer.save()