from rest_framework import generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from product.serializers import ProductListSerializer
from category.models import Category
from . import serializers


# Create your views here.
class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


    def get_permission(self):
        if self.request.method == 'GET':
            return permissions.AllowAny(),
        return permissions.IsAdminUser(),



class CategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return permissions.AllowAny(),
        return permissions.IsAdminUser(),

    @action(['GET'], detail=True)
    def products(self, request, pk):
        category = self.get_object()
        products = category.product.all()
        serializer = ProductListSerializer(instance=products, many=True)
        return Response(serializer.data, status=200)

    @action(['DELETE'], detail=True)
    def perform_destroy(self, instance):
        category = instance.category
        instance.delete()
        category.delete()
        return Response('Successfully deleted', status=200)