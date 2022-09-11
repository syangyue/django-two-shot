from django.contrib.auth.models import User
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import authenticate, login
from django.views.generic.base import LoginView, LogoutView
from .views import signup


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", signup, name="signup")
]
