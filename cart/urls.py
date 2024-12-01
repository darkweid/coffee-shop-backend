from django.urls import path
from .views import CartAddView, CartDeleteView, CartClearView

urlpatterns = [
    path('cart', CartAddView.as_view(), name='cart-add'),
    path('cart/<int:pk>', CartDeleteView.as_view(), name='cart-delete'),
    path('cart', CartClearView.as_view(), name='cart-clear'),
]
