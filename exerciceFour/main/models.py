from django.db import models

# Create your models here.


class Products(models.Model):
    productImg = models.TextField()
    productName = models.CharField(max_length=120)
    productPrice = models.DecimalField(decimal_places=2, max_digits=8)
    productQnt = models.IntegerField()


class CartHistory(models.Model):
    dateBuy = models.DateTimeField(auto_now_add=True)
    totalPrice = models.DecimalField(decimal_places=2, max_digits=8)


class ProductBought(models.Model):
    productFk = models.ForeignKey(Products, on_delete=models.CASCADE)
    cartFk = models.ForeignKey(CartHistory, on_delete=models.CASCADE)
    quantity = models.IntegerField()
