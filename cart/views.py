from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from product.permissions import IsUserOrAdmin
from . import serializers
from .models import Cart

User = get_user_model()

class OrderCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.OrderCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderRemoveView(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsUserOrAdmin)
    serializer_class = serializers.OrderRemoveSerializer

    def perform_destroy(self, instance):
        instance.delete()

class OrderListView(APIView):
    permission_classes = (permissions.IsAuthenticated, IsUserOrAdmin)
    @action(['GET'], detail=True)
    def get(self, request):
        orders = request.user.orders.all()
        serializer = serializers.OrderListSerializer(instance=orders, many=True, context=request.user).data
        serializer = [x for x in serializer]
        return Response(serializer, status=200)
