from django.db import models
from django.conf import settings

class ProductView(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="product_views"
    )
    session_key = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        help_text="Used to track anonymous users"
    )
    product_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['product_id']),
            models.Index(fields=['user']),
            models.Index(fields=['timestamp']),
        ]

    def __str__(self):
        identity = self.user.email if self.user else f"Session {self.session_key}"
        return f"Product {self.product_id} viewed by {identity} at {self.timestamp}"
