from django.db.models import Count
from .models import Category


def count_by_category():
    return Category.objects.annotate(amount=Count('medication')).values('id', 'name', 'amount').all()
