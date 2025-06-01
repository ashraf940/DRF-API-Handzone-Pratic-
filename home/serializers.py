from rest_framework import serializers
from .models import People, Color
from django.contrib.auth.models import User



class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError("Username already exists")
        
        if data['email']:
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError("email already exists")
        return data
    def create(self,validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'] )
        user.save()
        return validated_data
        print(validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name', 'id']


class PeopleSerializer(serializers.ModelSerializer):
    # If you want nested color details uncomment below
    # color = ColorSerializer(read_only=True)

    class Meta:
        model = People
        fields = '__all__'
        # depth = 1  # optionally use this for nested relationships

    def get_color_info(self, obj):
        if obj.color:
            return {
                'color_name': obj.color.color_name,
                'hex_code': '#000'
            }
        return {
            'color_name': None,
            'hex_code': None
        }

    def validate(self, data):
        special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"
        if any(c in special_characters for c in data.get('name', '')):
            raise serializers.ValidationError("Name cannot contain special characters")

        if data.get('age', 0) < 18:
            raise serializers.ValidationError("Age must be greater than 18")
        return data
