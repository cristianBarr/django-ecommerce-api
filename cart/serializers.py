from rest_framework import serializers
from .models import Cart, CartItem
from products.serializers import ProductSerializer 

class CartItemSerializer(serializers.ModelSerializer): # CartItem a JSON para la API
    product = ProductSerializer(read_only=True)
    total_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']


class CartSerializer(serializers.ModelSerializer): #Cart completo a JSON para la API
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price', 'created_at']


