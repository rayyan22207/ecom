from django.db import models
from django.conf import settings
from catalog.models import Product


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    rating = models.PositiveSmallIntegerField()  # 1 to 5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)  # You can moderate if needed

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.rating}⭐ by {self.user.email if self.user else 'Guest'}"
