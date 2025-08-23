from django.test import TestCase
from ..models import Product, Category

class ProductModelTest(TestCase): #Test para el modelo Product
    def test_crear_producto_simple(self): #Test para crear producto bàsico
        producto = Product.objects.create(
            name="Laptop Gaming",
            price=1500.00,
            sku="LAPTOP-001"
        )
        #Verificaciones
        self.assertEqual(producto.name, "Laptop Gaming")
        self.assertEqual(producto.price, 1500.00)
        self.assertEqual(producto.stock, 0) #Valor por defecto
        self.assertTrue(producto.is_active) #True por defecto

    def test_string_representation(self): #Test representaciòn en string del producto
        producto = Product.objects.create(
            name="Tablet",
            price=300.00,
            sku="TAB-001"
        )
        self.assertEqual(str(producto), "Tablet (TAB-001)")

