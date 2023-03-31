from django.urls import path
from . import views
from dj_rest_auth.views import LoginView


urlpatterns = [
    path('register/', views.RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
]