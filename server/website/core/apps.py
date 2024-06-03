from django.contrib.admin.apps import AdminConfig


class CustomizeAdminConfig(AdminConfig):
    default_site = "core.admin.CustomizeAdminSite"