from django.urls import path
from .api_views import OrderListView, OrderDetailView
from . import views

urlpatterns = [
    path("api/", OrderListView.as_view(), name="order-list"),
    path("api/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
]
