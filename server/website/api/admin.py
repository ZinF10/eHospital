from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (
    User, Patient, Tag, Department, Doctor, Nurse, 
    Category, Medication, Experience, Award, Department
)
from .inlines import (
    TagMedicationInline, MedicationInline, ExperienceInline,
    AwardInline, TagDoctorInline, TagNurseInline, NurseInline,
    DotorInline
)
from .actions import export_as_json, make_actived, export_as_csv
from .forms import UserChangeForm, UserCreationForm


class BaseAdmin(admin.ModelAdmin):
    empty_value_display = "-Unknown-"
    list_display = ["is_active", "date_created", "date_updated"]
    ordering = ["date_created", "id"]
    date_hierarchy = "date_created"
    list_per_page = 10
    list_filter = ["is_active"]


class ItemAdmin(BaseAdmin):
    prepopulated_fields = {"slug": ["name"]}
    ordering = BaseAdmin.ordering
    search_fields = ["slug"]
    list_filter = BaseAdmin.list_filter


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


class UserAdmin(BaseUserAdmin, BaseAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["username", "avatar_preview",
                    "role", "is_active", "last_login"]
    date_hierarchy = "date_joined"
    list_editable = ["is_active"]
    search_fields = ['email', 'username', 'first_name', 'last_name']
    list_filter = ["is_superuser", "is_active", "is_staff", "role"]

    fieldsets = [
        (None, {"fields": ["email", "username", "password"]}),
        ('Personal Info', {"fields": [
         "first_name", "last_name", "avatar", "is_active", "date_joined", "last_login"]}),
        ("Permissions", {"fields": [
         "is_superuser", "is_staff", "role", "user_permissions"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password", "confirm_password",
                           "avatar", "username", "first_name", "last_name", "role",
                           "is_active", "is_staff", "is_superuser", "user_permissions"],
            },
        ),
    ]
    ordering = ["email", "first_name", "last_name"]
    filter_horizontal = ['user_permissions']
    readonly_fields = ["avatar_preview"]


class PatientAdmin(BaseAdmin):
    list_display = ["user", "gender", "phone",
                    "blood_group"] + BaseAdmin.list_display
    search_fields = ["user__first_name",
                     "user__last_name", "phone", "location"]
    list_filter = ["gender", "blood_group",
                   "date_of_birth"] + BaseAdmin.list_filter


class DepartmentAdmin(ItemAdmin):
    inlines = [NurseInline, DotorInline]
    list_display = ["name", "description"] + ItemAdmin.list_display
    search_fields = ["name"] + ItemAdmin.search_fields
    list_filter = ["name"] + ItemAdmin.list_filter


class DoctorAdmin(BaseAdmin):
    inlines = [TagDoctorInline, ExperienceInline, AwardInline]
    exclude = ["tags"]
    list_display = ["user", "department"] + BaseAdmin.list_display
    search_fields = ["user__first_name",
                     "user__last_name", "department__name", "phone"]
    list_filter = ["department"] + BaseAdmin.list_filter


class NurseAdmin(BaseAdmin):
    inlines = [TagNurseInline]
    exclude = ["tags"]
    list_display = ["user", "department"] + BaseAdmin.list_display
    search_fields = ["user__first_name",
                     "user__last_name", "department__name", "phone"]
    list_filter = ["department"] + BaseAdmin.list_filter


class ExperienceAdmin(BaseAdmin):
    list_display = ["doctor", "hospital", "position",
                    "start_date", "end_date"] + BaseAdmin.list_display
    search_fields = ["doctor__user__first_name", "doctor__user__last_name",
                     "hospital", "position"]
    list_filter = ["hospital", "position"] + BaseAdmin.list_filter


class AwardAdmin(BaseAdmin):
    list_display = ["doctor", "title",
                    "date_received"] + BaseAdmin.list_display
    search_fields = ["doctor__user__first_name",
                     "doctor__user__last_name", "title"]
    list_filter = ["title", "date_received"] + BaseAdmin.list_filter


admin.site.register(User, UserAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Nurse, NurseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Medication, MedicationAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Permission)
admin.site.add_action(export_as_json, "export_as_json")
admin.site.add_action(export_as_csv, "export_as_csv")
admin.site.add_action(make_actived, "mark_actived")
