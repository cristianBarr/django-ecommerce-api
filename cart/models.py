from django.db import models
from django.contrib.auth.models import User
from products.models import Product  # ← Importamos Product de otra app

class Cart(models.Model):
    """Carrito de compras - Puede ser de usuario o sesión"""
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name='cart'
    )
    session_key = models.CharField(
        max_length=40, 
        null=True, 
        blank=True,
        help_text="Para usuarios no logueados"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"

    def __str__(self):
        if self.user:
            return f"Carrito de {self.user.username}"
        return f"Carrito de sesión {self.session_key}"

    def total_price(self):
        """Calcula el precio total sumando todos los items"""
        return sum(item.total_price() for item in self.items.all())


class CartItem(models.Model):
    """Items individuales dentro del carrito"""
    cart = models.ForeignKey(
        Cart, 
        on_delete=models.CASCADE,
        related_name='items'  # ← Acceso: carrito.items.all()
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        related_name='cart_items'
    )
    quantity = models.PositiveIntegerField(
        default=1,
        help_text="Cantidad de este producto en el carrito"
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Item de Carrito"
        verbose_name_plural = "Items de Carrito"
        unique_together = ['cart', 'product']  # ← Evita duplicados

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def total_price(self):
        """Precio total de este item (precio * cantidad)"""
        return self.product.price * self.quantity