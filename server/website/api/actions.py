import csv
from django.contrib import admin, messages
from django.utils.translation import ngettext
from django.http import HttpResponse
from django.core import serializers


@admin.action(description="Mark selected model as deactived", permissions=["change"])
def make_actived(self, request, queryset):
    updated = queryset.update(is_active=False)
    self.message_user(
        request,
        ngettext(
            "%d model was successfully marked as actived.",
            "%d models were successfully marked as actived.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


@admin.action(permissions=["change"], description="Export as JSON")
def export_as_json(self, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response


@admin.action(permissions=["change"], description="Export as CSV")
def export_as_csv(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
        meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response