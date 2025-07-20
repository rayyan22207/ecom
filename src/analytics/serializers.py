from rest_framework import serializers
from .models import ProductView
from django.contrib.auth import get_user_model

User = get_user_model()


class ProductViewSerializer(serializers.ModelSerializer):
    user_email = serializers.SerializerMethodField()

    class Meta:
        model = ProductView
        fields = [
            'id',
            'user_email',
            'session_key',
            'product_id',
            'timestamp',
        ]
        read_only_fields = ['id', 'timestamp', 'user_email']

    def get_user_email(self, obj):
        return obj.user.email if obj.user else None
