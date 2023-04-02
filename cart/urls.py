from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', views.OrderCreateView.as_view()),
    path('orders/', views.OrderListView.as_view()),

]