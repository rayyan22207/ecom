from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("auth.urls")),
    path("accounts/", include('allauth.urls')),
    path("checkouts/", include('checkouts.urls')),
    path("customers/", include('customers.urls')),
    path("dashboard/", include('dashboard.urls')),
]
