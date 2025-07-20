from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)




urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("accounts.urls")),
    path("accounts/", include('allauth.urls')),
    path("checkouts/", include('checkouts.urls')),
    path("dashboard/", include('dashboard.urls')),
    path("catalog/", include("catalog.urls")),
    path("cart/", include('cart.urls')),
    path("orders/", include('orders.urls')),
    path("comments/", include('comments.urls')),
    path("analytics/", include('analytics.urls')),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
