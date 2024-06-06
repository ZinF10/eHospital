from rest_framework.pagination import PageNumberPagination


class BaseSetPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 1000


class LargeResultsSetPagination(BaseSetPagination):
    page_size = 100


class StandardResultsSetPagination(BaseSetPagination):
    page_size = 10


class SmallResultsSetPagination(BaseSetPagination):
    page_size = 5
