from django.db.models import Count
from .models import Category, Medication, Patient, User, Doctor, Nurse, Department


def load_departments():
    return Department.objects.filter(is_active=True).all().order_by('-date_created')


def load_categories():
    return Category.objects.filter(is_active=True).all()


def load_medications():
    return Medication.objects.select_related('category').prefetch_related('tags').filter(is_active=True)


def load_patients():
    return Patient.objects.select_related('user').filter(is_active=True)


def load_doctors():
    return Doctor.objects.select_related('department', 'user').prefetch_related('tags').filter(is_active=True)


def load_users():
    return User.objects.filter(is_active=True).all().order_by('-date_joined')


def stats_amount_medications():
    return Category.objects.annotate(amount=Count('medication')).values('id', 'name', 'amount').all()
