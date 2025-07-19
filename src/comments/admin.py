from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user_email", "rating", "is_approved", "created_at")
    list_filter = ("is_approved", "rating", "created_at")
    search_fields = ("user__email", "product__name", "comment")
    readonly_fields = ("created_at",)

    def user_email(self, obj):
        return obj.user.email if obj.user else "Guest"
    user_email.short_description = "User Email"
