from django.shortcuts import render
from .serializers import CustomSerializer
from rest_framework import viewsets
from users.models import Custom

# Create your views here.

class CustomView(viewsets.ModelViewSet):
    queryset = Custom.objects.all()
    serializer_class = CustomSerializer