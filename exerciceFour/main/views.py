from django.shortcuts import render
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class ProductsView(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    ordering_fields = '__all__'


class CartHistoryView(ModelViewSet):
    queryset = CartHistory.objects.all()
    serializer_class = CartHistorySerializer
    filter_backends = [DjangoFilterBackend]
    ordering_fields = '__all__'


class ProductBoughtView(ModelViewSet):
    queryset = ProductBought.objects.all()
    serializer_class = ProductBoughtSerializer
    filter_backends = [DjangoFilterBackend]
    ordering_fields = '__all__'
