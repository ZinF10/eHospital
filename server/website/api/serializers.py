from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .dao import load_categories, load_patients, load_doctors, load_departments
from .models import Category, Medication, User, Patient, Doctor, Nurse
from .utils import send_custom_email, generate_reset_code


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = ['slug']


class InforSerializer(BaseSerializer):
    class Meta:
        model = BaseSerializer.Meta.model
        fields = BaseSerializer.Meta.fields + ["phone"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'avatar', 'password']
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


class CurrentUserSerializer(UserSerializer):
    role = GroupSerializer(read_only=True)
    class Meta:
        model = UserSerializer.Meta.model
        fields = UserSerializer.Meta.fields + ['role', 'last_login']
        extra_kwargs = UserSerializer.Meta.extra_kwargs


class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True, style={
        'input_type': 'password'})
    new_password = serializers.CharField(
        write_only=True, required=True, style={'input_type': 'password'})

    def validate(self, data):
        if data['old_password'] == data['new_password']:
            raise serializers.ValidationError(
                "New password must be different from the old password.")
        return data


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, write_only=True)

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User does not exist.")
        return value

    def save(self):
        email = self.validated_data['email']
        user = User.objects.filter(email=email).first()
        reset_code = generate_reset_code(user=user)
        message = f"""
                Hey ✌️, {user.last_name} {user.first_name}\n
                We've sent you the code: {reset_code} to reset your password.\n
                𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃\n
                Code: {reset_code}\n
                𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃\n
                Have A Good Day ❤️.
                """
        send_custom_email(subject="Password Reset Code 🔒",
                          message=message, recipients=[email])


class ResetPasswordserializer(serializers.Serializer):
    reset_code = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True, style={
        'input_type': 'password'})

    def validate_reset_code(self, value):
        if not User.objects.filter(reset_code=value).exists():
            raise serializers.ValidationError(
                "Reset Code is invalid or expired")
        return value

    def save(self):
        reset_code = self.validated_data['reset_code']
        new_password = self.validated_data['new_password']
        user = User.objects.filter(reset_code=reset_code).first()
        user.set_password(new_password)
        user.reset_code = None
        user.save()


class PatientSerializer(InforSerializer):
    user = UserSerializer(required=True)
    slug = serializers.SlugField(
        read_only=True,
        validators=[UniqueValidator(queryset=load_patients())]
    )

    class Meta:
        model = Patient
        fields = ["user", "slug", "gender", "location", "date_of_birth"] + \
            InforSerializer.Meta.fields

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        patient = Patient.objects.create(user=user, **validated_data)
        return patient


class DoctorSerializer(InforSerializer):
    user = UserSerializer(read_only=True)
    slug = serializers.SlugField(
        read_only=True,
        validators=[UniqueValidator(queryset=load_doctors())]
    )
    department = serializers.StringRelatedField(many=False)

    class Meta:
        model = Doctor
        fields = ["user", "slug", "price", "description"] + \
            InforSerializer.Meta.fields + ["department"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['slug', 'name']


class MedicationSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Medication
        fields = ['slug', 'name', 'price', 'description', 'category']
