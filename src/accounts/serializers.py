from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile, Address

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone', 'avatar', 'marketing_opt_in']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id', 'label', 'full_name', 'line1', 'line2',
            'city', 'state', 'postal_code', 'country',
            'is_default_shipping', 'is_default_billing'
        ]


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)
    addresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'email_verified', 'is_active', 'is_staff', 'date_joined',
            'profile', 'addresses'
        ]
        read_only_fields = ['is_active', 'is_staff', 'email_verified', 'date_joined']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ['email', 'password', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        Profile.objects.create(user=user, **profile_data)
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, min_length=8)
