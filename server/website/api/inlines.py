from django.contrib import admin
from .models import Medication, Experience, Award, Doctor, Nurse


class MedicationInline(admin.StackedInline):
    model = Medication


class TagMedicationInline(admin.TabularInline):
    model = Medication.tags.through


class TagDoctorInline(admin.TabularInline):
    model = Doctor.tags.through


class TagNurseInline(admin.TabularInline):
    model = Nurse.tags.through


class ExperienceInline(admin.StackedInline):
    model = Experience


class AwardInline(admin.StackedInline):
    model = Award


class NurseInline(admin.StackedInline):
    model = Nurse


class DotorInline(admin.StackedInline):
    model = Doctor
