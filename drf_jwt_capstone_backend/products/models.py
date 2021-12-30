from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    salesPrice = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    manufacturingCost = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    aisleName = models.CharField(max_length=30 , blank=True, null=True)
