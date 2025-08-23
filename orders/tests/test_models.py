from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Order

class OrderModelTest(TestCase):
    def test_crear_orden(self):
        user = User.objects.create_user('testuser', 'test@example.com', 'password')
        order = Order.objects.create(user=user, total=100.00)
        self.assertEqual(order.status, 'pending') #Valor por defecto
        
        

