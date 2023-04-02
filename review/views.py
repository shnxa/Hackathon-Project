from django.shortcuts import render
from rest_framework import generics, permissions
from . import serializers
from .models import Review
from product.permissions import IsUserOrAdmin

class ReviewCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.ReviewCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewDetailSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return IsUserOrAdmin(),
        return permissions.AllowAny(),