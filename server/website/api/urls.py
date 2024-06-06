from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from django.views.i18n import set_language
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'medications', views.MedicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("chart/categories/", views.get_stats_categories, name="chart-categories"),
    path('set-language/', set_language, name='set_language'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
