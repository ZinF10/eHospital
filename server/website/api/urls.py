from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("chart/categories/", views.get_stats_categories, name="chart-categories"),
]
