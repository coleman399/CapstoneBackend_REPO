from django.db import models

# Create your models here.
class Product(models.Model):
    productId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20, blank=True, null=True)
    description=models.TextField(max_length=300, blank=True, null=True)
    salesPrice=models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    manufactureringCost=models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    aisleName=models.ForeignKey('aisles.Aisle', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name