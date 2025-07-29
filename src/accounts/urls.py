from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api_views import (
    RegisterView, MeView, ChangePasswordView,
    AddressListCreateView, AddressDetailView
)
from . import views 

urlpatterns = [
    # JWT Auth
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Registration and profile
    path("api/register/", RegisterView.as_view(), name="register"),
    path("api/me/", MeView.as_view(), name="me"),
    path("api/change-password/", ChangePasswordView.as_view(), name="change-password"),

    # Address endpoints
    path("api/addresses/", AddressListCreateView.as_view(), name="address-list-create"),
    path("api/addresses/<int:pk>/", AddressDetailView.as_view(), name="address-detail"),
]
