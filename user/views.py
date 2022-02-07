from django.shortcuts import render
from .serializers import ForgotSerializer, UserSerializer, EmpSerializer
from rest_framework import viewsets, permissions, status
from .models import User, Emp
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_class = [MultiPartParser, FormParser]
    
    def get(self, request):
        user = User.objects.filter(email=request.user)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


class EmpView(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

    def get_user(self, request):
        user = request.user
        print(user)


class EmpIdView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_class = [MultiPartParser, FormParser]

    def post(self, request, format=None):

        serializer = EmpSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForgotView(APIView):
    parser_class = [MultiPartParser, FormParser]

    def post(self, request):

        serializer = ForgotSerializer(data=request.data)
        print(serializer)