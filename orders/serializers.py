from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer  # Para mostrar info de productos

class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer para items de orden"""
    product = ProductSerializer(read_only=True)  # Info completa del producto
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price', 'subtotal']

class OrderSerializer(serializers.ModelSerializer):
    """Serializer para órdenes con items incluidos"""
    items = OrderItemSerializer(many=True, read_only=True)  # ✅ Items anidados
    user = serializers.StringRelatedField(read_only=True)  # Solo nombre usuario
    
    class Meta:
        model = Order
        fields = [
            'id', 'user', 'status', 'total', 
            'created_at', 'updated_at', 'items'  # ✅ Incluir items
        ]
        read_only_fields = ['user', 'total', 'created_at', 'updated_at']  # Campos auto