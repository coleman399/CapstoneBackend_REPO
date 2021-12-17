from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Budget(models.Model):
    user= models.ManyToManyField(User, blank=True)
    total_sales = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    total_expenses = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    total_profit = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)