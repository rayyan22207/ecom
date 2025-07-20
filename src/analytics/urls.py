from django.urls import path
from .views import ProductViewCreateAPIView

urlpatterns = [
    path('track/', ProductViewCreateAPIView.as_view(), name='track-product-view'),
]
