from django.shortcuts import render
from rest_framework import permissions, generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response

# from .send_email import send_confirmation_mail
from account import serializers





class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegistrationSerializer