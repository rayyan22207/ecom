from django.contrib import admin
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ('product', 'variant', 'quantity', 'get_total_price')
    can_delete = True
    show_change_link = True


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_or_session', 'created_at', 'total_items')
    search_fields = ('user__email', 'session_key')
    list_filter = ('created_at',)
    inlines = [CartItemInline]
    readonly_fields = ('user', 'session_key', 'created_at')

    def user_or_session(self, obj):
        return obj.user.email if obj.user else f"Session: {obj.session_key}"
    user_or_session.short_description = "Owner"

    def total_items(self, obj):
        return obj.items.count()
    total_items.short_description = "Items in Cart"


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'variant', 'quantity', 'cart_id', 'get_total_price')
    search_fields = ('product__name', 'cart__user__email')
    list_filter = ('product',)

    def cart_id(self, obj):
        return obj.cart.id
    cart_id.short_description = "Cart ID"
