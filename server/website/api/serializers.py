from rest_framework import serializers
from .dao import load_categories
from .models import Category, Medication


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['slug', 'name']


class MedicationSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=load_categories())

    class Meta:
        model = Medication
        fields = ['slug', 'name', 'is_active', 'price', 'description', 'category']
