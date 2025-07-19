from django.contrib import admin
from .models import ProductView


@admin.register(ProductView)
class ProductViewAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'user_or_session', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('product_id', 'user__email', 'session_key')
    ordering = ('-timestamp',)
    readonly_fields = ('product_id', 'user', 'session_key', 'timestamp')

    def user_or_session(self, obj):
        return obj.user.email if obj.user else f"Session: {obj.session_key}"
    user_or_session.short_description = "Viewer"
