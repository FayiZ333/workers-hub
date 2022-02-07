from django.shortcuts import render
from .serializers import FormSerializer
from rest_framework import viewsets, permissions, status
from .models import Form
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.


class Form1View(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class FormView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_class = [MultiPartParser, FormParser]

    def post(self, request, format=None):

        serializer = FormSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)