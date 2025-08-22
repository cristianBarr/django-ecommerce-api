from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'is_active']  # Campos visibles
    list_filter = ['is_active']  # Filtros laterales
    search_fields = ['name', 'sku']  # Búsqueda