from django.urls import path
from .api_views import PaymentListView, PaymentDetailView, PaymentCreateView
from . import views

urlpatterns = [
    path('api/', PaymentListView.as_view(), name='payment-list'),
    path('api/create/', PaymentCreateView.as_view(), name='payment-create'),
    path('api/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
]
