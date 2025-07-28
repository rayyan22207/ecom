from django.urls import path
from .api_views import (
    CategoryListView,
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
    ProductVariantListView,
    ProductImageListView,
)
from . import views

urlpatterns = [
    
    
    
    # API endpoints for catalog
    path('api/categories/', CategoryListView.as_view(), name='category-list'),
    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('api/products/<int:product_id>/variants/', ProductVariantListView.as_view(), name='product-variants'),
    path('api/products/<int:product_id>/images/', ProductImageListView.as_view(), name='product-images'),
]
