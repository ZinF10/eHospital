from django.db.models import Count
from .models import Category, Medication, Patient


def load_categories():
    return Category.objects.filter(is_active=True).all().order_by('-date_created')


def load_medications():
    return Medication.objects.filter(is_active=True).all().order_by('-date_created')


def load_patients():
    return Patient.objects.filter(is_active=True).all().order_by('-date_created')


def stats_amount_medications():
    return Category.objects.annotate(amount=Count('medication')).values('id', 'name', 'amount').all()
