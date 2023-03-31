from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from product.models import Product
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from category import serializers
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
            return serializers.ProductListSerializer
        elif self.action in ('create', 'update', 'partial_update'):
            return serializers.ProductCreateSerializer
        return serializers.ProductDetailSerializer


    def get_permissions(self):
        if self.action in ('destroy', 'create', 'update', 'partial_update'):
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    @action(['POST', 'DELETE'], detail=True)
    def favorite(self, request, pk):
        product = self.get_object()
        user = request.user
        if request.method == 'POST':
            if user.favorites.filter(product=product).exists():
                return Response('You\'ve already saved this product!', status=400)
            Favorites.objects.create(user=user, product=product)
            return Response('Successfully saved this product!', status=201)
        else:
            favorite = user.favorites.filter(product=product)
            if favorite.exists():
                favorite.delete()
                return Response('Successfully removed from favorites!', status=204)
            return Response('You don\'t have this product saved!', status=400)
