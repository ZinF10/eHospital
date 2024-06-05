from rest_framework_csv.renderers import CSVRenderer


class CategoryRenderer(CSVRenderer):
    header = '__all__'
