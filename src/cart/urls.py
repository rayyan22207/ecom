from django.urls import path
from .api_views import CartRetrieveView, CartItemAddView, CartItemDeleteView, CartItemUpdateView
from . import views

urlpatterns = [
    path('api/', CartRetrieveView.as_view(), name='cart-detail'),
    path('api/add/', CartItemAddView.as_view(), name='cart-add-item'),
    path('api/item/<int:pk>/delete/', CartItemDeleteView.as_view(), name='cart-delete-item'),
    path('api/item/<int:pk>/update/', CartItemUpdateView.as_view(), name='cart-update-item'),
]
