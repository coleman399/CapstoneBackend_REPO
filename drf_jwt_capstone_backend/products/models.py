from django.db import models

# Create your models here.
class Aisle(models.Model):
    aisleName = models.CharField(max_length=20)
    
    def __str__(self):
        return self.aisleName

class Product(models.Model):
    productId=models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    salesPrice = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    manufactureringCost = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    aisleName = models.ManyToManyField(Aisle, blank=True)
    
    def __str__(self):
        return self.name