from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from .models import User, Profile, Address

# Inline for Profile
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"
    fk_name = "user"
    extra = 0


# Inline for Addresses
class AddressInline(admin.StackedInline):
    model = Address
    verbose_name_plural = "Addresses"
    extra = 0


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    inlines = [ProfileInline, AddressInline]
    list_display = ("email", "email_verified", "is_staff", "is_active", "date_joined")
    list_filter = ("is_staff", "is_superuser", "is_active", "email_verified", "date_joined")
    search_fields = ("email",)
    ordering = ("-date_joined",)
    readonly_fields = ("date_joined",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("date_joined",)}),
        (_("Verification"), {"fields": ("email_verified",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_active")}
        ),
    )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super().get_inline_instances(request, obj)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("full_name", "user", "label", "city", "country", "is_default_shipping", "is_default_billing")
    list_filter = ("label", "city", "country", "is_default_shipping", "is_default_billing")
    search_fields = ("full_name", "city", "state", "postal_code", "country")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "marketing_opt_in")
    search_fields = ("user__email", "phone")
