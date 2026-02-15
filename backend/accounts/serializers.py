from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            phone_number=data['phone_number'],
            password=data['password']
        )
        if not user:
            raise serializers.ValidationError("Identifiants incorrects")
        return user

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ["phone_number", "fullname", "password", "role"]

    def create(self, validated_data):
        validated_data["role"] = "owner"
        user = User(
            phone_number=validated_data["phone_number"],
            fullname=validated_data.get("fullname", ""),
            role=validated_data["role"]

           
             # ce compte est un propriétaire de salon
        )
        user.set_password(validated_data["password"])
        user.save()
        return user