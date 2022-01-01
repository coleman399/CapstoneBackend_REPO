from django.db import models


# Create your models here.
class Budget(models.Model):
    date= models.DateField(auto_now_add=True)
    total_sales = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    total_expenses = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    total_profit = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)