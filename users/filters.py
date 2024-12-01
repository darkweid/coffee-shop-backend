from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters

User = get_user_model()


class UserFilter(filters.FilterSet):
    email = filters.CharFilter(lookup_expr='icontains')
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    is_active = filters.BooleanFilter()
    date_joined = filters.DateFromToRangeFilter()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'is_active', 'date_joined']
