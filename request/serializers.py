from pyexpat import model
from rest_framework import serializers
from .models import Form


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ('id','category','district','city', 'address', 'phone', 'time_from', 'time_to', 'requierments', 'budget')