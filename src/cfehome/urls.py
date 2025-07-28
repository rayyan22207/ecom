from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)




urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("accounts.urls")),
    path("api/accounts/", include('allauth.urls')),
    path("api/checkouts/", include('checkouts.urls')),
    path("dashboard/", include('dashboard.urls')),
    path("api/catalog/", include("catalog.urls")),
    path("api/cart/", include('cart.urls')),
    path("api/orders/", include('orders.urls')),
    path("api/comments/", include('comments.urls')),
    path("api/analytics/", include('analytics.urls')),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    
    # 🧠 API schema (JSON)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # 💠 Swagger UI (Interactive)
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # 📘 Redoc UI (Clean, docs-style)
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
