from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination


from product.models import Product
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from product import serializers
from rest_framework.response import Response

class StandardResultPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    pagination_class = StandardResultPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title',)
    filterset_fields = ('author', 'category')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductDetailSerializer
        elif self.action == 'create':
            return serializers.ProductCreateSerializer
        return serializers.ProductListSerializer


    def get_permissions(self):
        if self.action in ('destroy', 'create', 'update', 'partial_update'):
            return [permissions.IsAdminUser()]
        elif self.action == 'list':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    # @action(['POST'], detail=True)
    # def add_cart(self, request, pk):
    #     product = self.get_object()
    #     user = request.user
    #     if request.method == 'POST':
    #         Cart.objects.create(user=user, product=product)
    #         return Response('Successfully saved this product to your shopping basket!', status=201)
    #
