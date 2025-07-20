from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


class CartRetrieveView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        user = request.user if request.user.is_authenticated else None
        session_key = request.session.session_key or request.session.create() or request.session.session_key

        cart, _ = Cart.objects.get_or_create(user=user if user else None, session_key=None if user else session_key)

        serializer = CartSerializer(cart)
        return Response(serializer.data)


class CartItemAddView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        session_key = self.request.session.session_key or self.request.session.create() or self.request.session.session_key

        cart, _ = Cart.objects.get_or_create(user=user if user else None, session_key=None if user else session_key)
        serializer.save(cart=cart)


class CartItemDeleteView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CartItemSerializer


class CartItemUpdateView(generics.UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.AllowAny]
