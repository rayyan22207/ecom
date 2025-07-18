from django.db import models
from django.conf import settings


class ProductView(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    product_id = models.IntegerField()  # Store ID only for speed (you can use FK if needed)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"View – Product {self.product_id} by {self.user or 'Anonymous'}"
