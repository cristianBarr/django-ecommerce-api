from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer  # ← Importación local

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer