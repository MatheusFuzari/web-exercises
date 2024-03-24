from rest_framework import serializers
from .models import *


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        many = True


class CartHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CartHistory
        fields = '__all__'
        many = True


class ProductBoughtSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBought
        fields = '__all__'
        many = True
