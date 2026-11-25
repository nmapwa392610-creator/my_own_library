from django.shortcuts import render
from .models import User
from .serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer