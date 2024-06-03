from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .settings import base
from .admin import admin_statistics_view

urlpatterns = [
    path("admin/statistics/", admin.site.admin_view(admin_statistics_view),
         name="admin-statistics"),
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]


if base.DEBUG:
    urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
