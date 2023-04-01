from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.CategoryCreateListView.as_view()),
    path('<int:pk>/', views.CategoryDetailsView.as_view()),
]