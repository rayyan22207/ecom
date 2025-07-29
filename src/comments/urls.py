from django.urls import path
from .api_views import ReviewListView, ReviewCreateView, ReviewDetailView
from . import views

urlpatterns = [
    path('api/', ReviewListView.as_view(), name='review-list'),
    path('api/create/', ReviewCreateView.as_view(), name='review-create'),
    path('api/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
