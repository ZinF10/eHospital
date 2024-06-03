from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import Category, Medication, Tag
from .inlines import TagMedicationInline, MedicationInline
from .actions import export_as_json, make_actived, export_as_csv

class BaseAdmin(admin.ModelAdmin):
    empty_value_display = "-Unknown-"
    list_display = ["is_active", "date_created", "date_updated"]
    ordering = ["date_created", "id"]
    date_hierarchy = "date_created"
    list_per_page = 10


class ItemAdmin(BaseAdmin):
    prepopulated_fields = {"slug": ["name"]}
    ordering = BaseAdmin.ordering
    search_fields = ["slug"]
    list_filter = ["is_active"]


class CategoryAdmin(ItemAdmin):
    inlines = [MedicationInline]
    list_display = ["name"] + ItemAdmin.list_display
    search_fields = ["name"] + ItemAdmin.search_fields


class MedicationAdmin(ItemAdmin):
    inlines = [TagMedicationInline]
    exclude = ["tags"]
    list_display = ["name", "price", "category"] + ItemAdmin.list_display
    list_select_related = ["category"]
    search_fields = ["name"] + ItemAdmin.search_fields
    list_filter = ["category", "price"]


class TagAdmin(BaseAdmin):
    list_display = ["name"] + BaseAdmin.list_display
    search_fields = ["name"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Medication, MedicationAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Permission)
admin.site.add_action(export_as_json, "export_as_json")
admin.site.add_action(export_as_csv, "export_as_csv")
admin.site.add_action(make_actived, "mark_actived")
