from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['productId', 'name', 'description', 'salesPrice', 'manufactureringCost', 'aisleName']