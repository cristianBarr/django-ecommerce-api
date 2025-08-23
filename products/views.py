from rest_framework import generics, filters as rest_filters
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters # type: ignore
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter

# Paginacion para no sobrecargar con muchos productos
class ProductPagination(PageNumberPagination):
    page_size = 20  # 20 productos por defecto
    page_size_query_param = 'page_size'  # Pueden cambiar esto desde la URL
    max_page_size = 100  # No mas de 100 por pagina

# Vista para listar y crear productos
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination  # Usa nuestra paginacion
    
    # Filtros y busqueda
    filter_backends = [
        filters.DjangoFilterBackend,  # Filtros especificos
        rest_filters.SearchFilter,    # Busqueda general
        rest_filters.OrderingFilter   # Ordenar resultados
    ]
    
    filterset_class = ProductFilter  # Nuestros filtros personalizados
    
    # Donde buscar cuando usan ?search=algo
    search_fields = ['name', 'sku', 'description']
    
    # Campos que se pueden ordenar
    ordering_fields = ['name', 'price', 'created_at']
    
    # Orden por defecto: mas nuevos primero
    ordering = ['-created_at']