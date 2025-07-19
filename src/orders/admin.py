from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product", "variant", "quantity", "price")
    can_delete = False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_email",
        "status",
        "subtotal",
        "shipping_cost",
        "total",
        "created_at",
    )
    list_filter = ("status", "created_at")
    search_fields = ("user__email", "id")
    date_hierarchy = "created_at"
    readonly_fields = ("created_at", "subtotal", "shipping_cost", "total")
    inlines = [OrderItemInline]

    def user_email(self, obj):
        return obj.user.email if obj.user else "Guest"
    user_email.short_description = "User Email"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "variant", "quantity", "price")
    search_fields = ("order__id", "product__name", "variant__name")
    list_filter = ("product",)
