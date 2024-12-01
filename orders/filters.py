from django_filters import rest_framework as filters
from .models import Order


class OrderFilter(filters.FilterSet):
    user = filters.CharFilter(field_name="user__email", lookup_expr="icontains")
    product = filters.CharFilter(field_name="product__name", lookup_expr="icontains")
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Order
        fields = ['user', 'product', 'created_at']
