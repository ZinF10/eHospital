from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import Category, Medication, User, Patient, Doctor
from .utils import send_custom_email, generate_reset_code
from .common import BaseSerializer, InforSerializer, ItemSerializer, UserSerializer

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class CurrentUserSerializer(UserSerializer):
    role = GroupSerializer(read_only=True)
    class Meta:
        model = UserSerializer.Meta.model
        fields = UserSerializer.Meta.fields + ['role', 'last_login']
        extra_kwargs = UserSerializer.Meta.extra_kwargs


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


class ResetPasswordserializer(serializers.Serializer):
    reset_code = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(
        write_only=True, required=True, style={'input_type': 'password'})
    
    def validate_reset_code(self, value):
        if not User.objects.filter(reset_code=value).exists():
            raise serializers.ValidationError(
                "Reset Code is invalid or expired")
        return value

    def save(self):
        reset_code = self.validated_data['reset_code']
        new_password = self.validated_data['new_password']
        user = User.objects.filter(reset_code=reset_code).first()
        if user:
            raise serializers.ValidationError("User not found with provided reset code")
        user.set_password(new_password)
        user.reset_code = None
        user.save()


class PatientSerializer(InforSerializer):
    class Meta:
        model = Patient
        fields = InforSerializer.Meta.fields + ["gender", "location", "date_of_birth"]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        patient = Patient.objects.create(user=user, **validated_data)
        return patient


class DoctorSerializer(InforSerializer):
    department = serializers.StringRelatedField(many=False)

    class Meta:
        model = Doctor
        fields = InforSerializer.Meta.fields + ["price", "description", "department"]


class CategorySerializer(BaseSerializer):
    class Meta:
        model = Category
        fields = BaseSerializer.Meta.fields + ['name']


class MedicationSerializer(ItemSerializer):
    class Meta:
        model = Medication
        fields = ItemSerializer.Meta.fields + ['price']
        

class MedicationDetailSerializer(MedicationSerializer):
    class Meta:
        model = MedicationSerializer.Meta.model
        fields = MedicationSerializer.Meta.fields + ["description"]