from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import viewsets, filters
from drf_excel.mixins import XLSXFileMixin
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers, dao, filters as customize_filters, paginators


@staff_member_required
def get_stats_categories(request):
    amount = [data["amount"]
              for data in dao.stats_amount_medications()]
    labels = [data["name"]
              for data in dao.stats_amount_medications()]

    return JsonResponse({
        "data":  {
            "labels": labels,
            "datasets": [{
                "data": amount,
                "label": "Amount"
            }]
        },
    })


class CategoryViewSet(XLSXFileMixin, viewsets.ReadOnlyModelViewSet):
    """
    This API returns a list of all **active** categories in the system.

    For more details on how categories are activated, please [see here](http://example.com/activating-accounts).
    """

    queryset = dao.load_categories()
    serializer_class = serializers.CategorySerializer
    lookup_field = 'slug'
    filename = 'categories.xlsx'
    pagination_class = None


class MedicationViewSet(XLSXFileMixin, viewsets.ReadOnlyModelViewSet):
    """
    This API returns a list of all **active** medications in the system.

    For more details on how medications are activated, please [see here](http://example.com/activating-accounts).
    """

    queryset = dao.load_medications()
    serializer_class = serializers.MedicationSerializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_class = customize_filters.MedicationFilter
    ordering_fields = ['price', 'name']
    search_fields = ['name']
    filename = 'medications.xlsx'
    pagination_class = paginators.StandardResultsSetPagination
