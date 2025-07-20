from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(source='order.id', read_only=True)

    class Meta:
        model = Payment
        fields = [
            'id',
            'order_id',
            'method',
            'status',
            'amount',
            'transaction_id',
            'paid_at',
        ]
        read_only_fields = ['status', 'paid_at']

class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['order', 'method', 'amount']
