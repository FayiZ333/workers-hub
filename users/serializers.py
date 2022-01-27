from django.db.models import fields
from rest_framework import serializers
from .models import Custom

class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom
        fields = ['id', 'first_name', 'last_name', 'email', 'address', 'phone', 'password']
        