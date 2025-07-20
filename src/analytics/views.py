from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import ProductView
from .serializers import ProductViewSerializer


class ProductViewCreateAPIView(generics.CreateAPIView):
    queryset = ProductView.objects.all()
    serializer_class = ProductViewSerializer
    permission_classes = [permissions.AllowAny]  # allow anonymous views too

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.create()
            session_key = self.request.session.session_key

        serializer.save(user=user, session_key=session_key)
