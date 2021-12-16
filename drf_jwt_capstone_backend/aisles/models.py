from django.db import models

# Create your models here.
class Aisle(models.Model):
    aisleId=models.AutoField(primary_key=True)
    aisleId=models.CharField(max_length=10)