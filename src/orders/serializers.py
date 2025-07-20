from rest_framework import serializers
from .models import Order, OrderItem
from catalog.models import ProductVariant
from catalog.serializers import ProductVariantSerializer  


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    variant = ProductVariantSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            "id", "product", "product_name", "variant", "quantity", "price"
        ]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user_email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Order
        fields = [
            "id", "user_email", "status", "shipping_address",
            "subtotal", "shipping_cost", "total", "created_at", "items"
        ]
        read_only_fields = ["subtotal", "shipping_cost", "total", "created_at", "user_email"]
