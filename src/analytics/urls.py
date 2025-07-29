from django.urls import path
from .api_views import ProductViewCreateAPIView
from . import views

urlpatterns = [
    path('api/track/', ProductViewCreateAPIView.as_view(), name='track-product-view'),
]
