from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from products.models import Product

class CartDetailView(generics.RetrieveAPIView): #Muestra el carrito del usuario actual
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self): # Obtiene o crea el carrito del usuario
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart
    

class AddToCartView(generics.CreateAPIView): # Agrega producto al carrito
    permission_classes = [permissions.IsAuthenticated] 

    def post(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        
        # Obtener producto
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Producto no encontrado"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Obtener o crear carrito
        cart, created = Cart.objects.get_or_create(user=user)
        
        # Agregar o actualizar item
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )
        
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        
        return Response(
            {"message": "Producto agregado al carrito"},
            status=status.HTTP_200_OK
        )  
    
