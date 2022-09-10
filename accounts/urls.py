from django.contrib.auth.models import User

from django.urls import path, include
from django.contrib.auth import authenticate, login
from django.views.generic.base import LoginView


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
]
