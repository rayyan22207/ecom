from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Review
        fields = [
            "id",
            "product",
            "user_email",
            "rating",
            "comment",
            "created_at",
            "is_approved",
        ]
        read_only_fields = ["user_email", "created_at", "is_approved"]
