from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    """
    Vista para listar y crear órdenes.
    - GET: Lista todas las órdenes del usuario autenticado
    - POST: Crea una nueva orden para el usuario autenticado
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Solo devuelve las órdenes del usuario actual
        """
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automáticamente asigna el usuario actual a la nueva orden
        """
        serializer.save(user=self.request.user)


class OrderDetailView(generics.RetrieveAPIView):
    """
    Vista para ver el detalle de una orden específica.
    - GET: Muestra los detalles de una orden (solo si pertenece al usuario)
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Solo permite ver órdenes que pertenecen al usuario actual
        """
        return Order.objects.filter(user=self.request.user)