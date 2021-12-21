from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)