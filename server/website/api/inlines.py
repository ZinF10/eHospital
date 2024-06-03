from django.contrib import admin
from .models import Medication


class MedicationInline(admin.StackedInline):
    model = Medication


class TagMedicationInline(admin.TabularInline):
    model = Medication.tags.through
