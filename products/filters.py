import django_filters
from .models import Category, Product


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name', 'description']


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    stock_min = django_filters.NumberFilter(field_name="stock", lookup_expr='gte')
    stock_max = django_filters.NumberFilter(field_name="stock", lookup_expr='lte')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['name', 'description', 'price_min', 'price_max', 'stock_min', 'stock_max', 'category']
