from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField("products.Product", blank=True)
    quantity = models.IntegerField(default=1)