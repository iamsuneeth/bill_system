from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product, Bill, BillItem
from .serializers import ListBillSerializer,CreateBillSerializer,ProductSerializer

# Create your views here.
class BillViewSet(ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = ListBillSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer