from django.contrib.auth.models import Group
from rest_framework import serializers
from .dao import load_categories
from .models import Category, Medication, User, Patient


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = ['slug']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    role = GroupSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'avatar', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        
        group, created = Group.objects.get_or_create(name="Patient")
        user.groups.add(group)
        user.role = group
        user.save()
        return user


class PatientSerializer(BaseSerializer):
    user = UserSerializer(required=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Patient
        fields = BaseSerializer.Meta.fields + ['user', 'address']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        patient = Patient.objects.create(user=user, **validated_data)
        return patient


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['slug', 'name']


class MedicationSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=load_categories())

    class Meta:
        model = Medication
        fields = ['slug', 'name', 'price', 'description', 'category']
