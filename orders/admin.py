from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):  # Mostrar items dentro de Order
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    inlines = [OrderItemInline]  # Items visibles dentro de Order