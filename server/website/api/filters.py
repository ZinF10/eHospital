from django_filters import rest_framework as filters
from .models import Medication


class MedicationFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    category = filters.CharFilter(
        field_name='category__slug', lookup_expr='icontains')
    active = filters.BooleanFilter(
        field_name='is_active', lookup_expr='exact')

    class Meta:
        model = Medication
        fields = ['min_price', 'max_price', 'category', 'active']