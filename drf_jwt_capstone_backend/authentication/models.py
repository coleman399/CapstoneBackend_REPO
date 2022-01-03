from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate
class User(AbstractUser):
    salary = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    spent = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    userPassword = models.CharField(max_length=20, blank=True, null=True)
