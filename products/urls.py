from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    ProductListCreateView, ProductDetailView
)

urlpatterns = [
    # Categories
    path('category', CategoryListCreateView.as_view(), name='category-list-create'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category-detail'),

    # Products
    path('product', ProductListCreateView.as_view(), name='product-list-create'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
]
