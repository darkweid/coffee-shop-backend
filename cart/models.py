from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart")
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Cart item {self.product.name} for {self.user.email}"
