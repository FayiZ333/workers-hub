from django.shortcuts import render
from .serializers import UserSerializer,EmpSerializer
from rest_framework import viewsets
from .models import User, Emp

# Create your views here.


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EmpView(viewsets.ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer