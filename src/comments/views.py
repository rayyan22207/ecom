from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.filter(is_approved=True)
    serializer_class = ReviewSerializer


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
