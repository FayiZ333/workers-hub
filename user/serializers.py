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
        fields = ( 'id','user', 'city', 'description', 'subscription', 'skill1', 'skill2', 'skill3', 'image')
