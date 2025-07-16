from rest_framework import generics
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # ¡Solo usuarios autenticados!