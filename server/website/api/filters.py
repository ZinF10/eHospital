from django_filters import rest_framework as filters
from .models import Medication, Doctor


class BaseFilter(filters.FilterSet):
    active = filters.BooleanFilter(
        field_name='is_active', lookup_expr='exact')
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    release_month = filters.NumberFilter(
        field_name='date_created', lookup_expr='month')
    release_month_after = filters.NumberFilter(
        field_name='date_created', lookup_expr='month__gt')
    release_month_before = filters.NumberFilter(
        field_name='date_created', lookup_expr='month__lt')

    class Meta:
        model = None
        fields = ['min_price', 'max_price', 'active', 'release_month',
                  'release_month_after', 'release_month_before']


class MedicationFilter(BaseFilter):
    category = filters.CharFilter(
        field_name='category__slug', lookup_expr='icontains')

    class Meta:
        model = Medication
        fields = ['category'] + BaseFilter.Meta.fields


class DoctorFilter(BaseFilter):
    department = filters.CharFilter(
        field_name='department__slug', lookup_expr='icontains')

    class Meta:
        model = Doctor
        fields = ['department'] + BaseFilter.Meta.fields
