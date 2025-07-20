from django.urls import path
from .views import CartRetrieveView, CartItemAddView, CartItemDeleteView, CartItemUpdateView

urlpatterns = [
    path('', CartRetrieveView.as_view(), name='cart-detail'),
    path('add/', CartItemAddView.as_view(), name='cart-add-item'),
    path('item/<int:pk>/delete/', CartItemDeleteView.as_view(), name='cart-delete-item'),
    path('item/<int:pk>/update/', CartItemUpdateView.as_view(), name='cart-update-item'),
]
