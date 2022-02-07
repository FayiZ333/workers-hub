from pyexpat import model
from rest_framework import serializers
from .models import User, Emp


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','password','email', 'address', 'phone')
        extra_kwargs = {'password':{'write_only':True}}
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class EmpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emp
        fields = [ 'id', 'city', 'description', 'subscription', 'skill', 'image']


class ForgotSerializer(serializers.ModelSerializer):

    class Meta:
        field = ['phone']



# class ProfileSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = User
#         fields = ('id','first_name','last_name','email', 'address', 'phone')