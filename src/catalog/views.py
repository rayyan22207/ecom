from rest_framework import generics, permissions
from .models import Category, Product, ProductImage, ProductVariant
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductImageSerializer,
    ProductVariantSerializer,
)

# ✅ Category Views (Public)
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


# ✅ Product Views
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


# ✅ Variant Views (Public GET)
class ProductVariantListView(generics.ListAPIView):
    serializer_class = ProductVariantSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        return ProductVariant.objects.filter(product_id=product_id)


# ✅ Image Views (Public GET)
class ProductImageListView(generics.ListAPIView):
    serializer_class = ProductImageSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        return ProductImage.objects.filter(product_id=product_id)
