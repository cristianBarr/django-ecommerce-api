from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    #Orden de compra con estado y total automàtico
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('paid', 'Pagado'),
        ('shipped', 'Enviado'),
        ('delivered', 'Entregado'),
        ('cancelled', 'Cancelado'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Òrdenes"
        ordering = ['-created_at']

    def __str__(self):
        return f"Orden #{self.id} - {self.user.username}"

    def calculate_total(self):
        #Calcular el total automáticamente basado en los items
        return sum(item.subtotal() for item in self.items.all())

    def save(self, *args, **kwargs):
        #Actualizar el total automáticamente antes de guardar
        if self.pk:  # Solo si la orden ya existe
            self.total = self.calculate_total()
        super().save(*args, **kwargs)

class OrderItem(models.Model):
    #Items individuales dentro de una orden
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  #Precio al momento de la compra

    class Meta:
        verbose_name = "Item de Orden"
        verbose_name_plural = "Items de Orden"

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def subtotal(self):
        """Calcular subtotal (precio * cantidad)"""
        return self.price * self.quantity