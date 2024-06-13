from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from .settings import base
from .admin import admin_statistics_view
admin.autodiscover()

urlpatterns = [
    path("admin/statistics/", admin.site.admin_view(admin_statistics_view),
         name="admin-statistics"),
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    re_path(r'mdeditor/', include('mdeditor.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider'))
]


if base.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls"))
    ] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
