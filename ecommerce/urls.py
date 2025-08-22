from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from products.views import ProductListCreateView
from orders.views import OrderListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', ProductListCreateView.as_view()),
    path('api/orders/', OrderListCreateView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]