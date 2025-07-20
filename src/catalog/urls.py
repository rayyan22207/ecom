from django.urls import path
from .views import (
    CategoryListView,
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
    ProductVariantListView,
    ProductImageListView,
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),

    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),

    path('products/<int:product_id>/variants/', ProductVariantListView.as_view(), name='product-variants'),
    path('products/<int:product_id>/images/', ProductImageListView.as_view(), name='product-images'),
]
