from django.db import models

# Create your models here.
class Aisle(models.Model):
    aisleId=models.AutoField(primary_key=True)
    aisleName=models.CharField(max_length=10)
    
    def __str__(self):
        return self.aisleName