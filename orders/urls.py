from django.urls import path
from .views import OrderListCreateView, OrderDetailView

urlpatterns = [
    path('order', OrderListCreateView.as_view(), name='order-list-create'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order-detail'),
]
