from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate
class Budget(models.Model):
    total_sales = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    total_expenses = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    total_profit = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)

class Role(models.Model):
    RoleName = models.TextChoices('RoleName','Customer Administrator')
    role=models.CharField(max_length=15, blank=True, choices=RoleName.choices)
    
    def __str__(self):
        return self.role

class User(AbstractUser):
    role_name = models.ManyToManyField(Role)
    budget = models.ManyToManyField(Budget, blank=True)

    def __str__(self):
        return self.role_name