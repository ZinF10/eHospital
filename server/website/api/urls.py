from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from django.views.i18n import set_language
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'medications', views.MedicationViewSet)
router.register(r'patients', views.PatientViewSet)
router.register(r'doctors', views.DoctorViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("chart/categories/", views.get_stats_categories, name="chart-categories"),
    path('set-language/', set_language, name='set_language'),
    path('openapi.yaml/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
