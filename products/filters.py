from django_filters import rest_framework as filters
from .models import Product

# Filtros personalizados para los productos
class ProductFilter(filters.FilterSet):
    # Filtro para precio minimo (mayor o igual)
    min_price = filters.NumberFilter(
        field_name="price", 
        lookup_expr='gte',  # gte = greater than or equal
        label='Precio mínimo'
    )
    
    # Filtro para precio maximo (menor o igual)  
    max_price = filters.NumberFilter(
        field_name="price",
        lookup_expr='lte',  # lte = less than or equal
        label='Precio máximo'
    )
    
    class Meta:
        model = Product
        # Campos que se pueden filtrar y como
        fields = {
            'category': ['exact'],  # Filtro exacto por categoria
            'price': ['gte', 'lte'],  # Para precios entre min y max
        }