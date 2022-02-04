from django.shortcuts import render
from .serializers import UserSerializer,EmpSerializer
from rest_framework import viewsets, permissions, status
from .models import User, Emp
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EmpView(viewsets.ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer


class EmpIdView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_class = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

