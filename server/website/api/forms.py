from .models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput,
                               help_text="Enter a password with more than 12 characters and contain special characters.")
    confirm_password = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput,
        help_text="Enter the same password as above, for verification."
    )

    class Meta:
        model = User
        fields = '__all__'

    def clean_password_custom(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords don't match")
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="Raw passwords are not stored, so there is no way to see this user's password, but you can change the password using <a href=\"password/\">this form</a>."
    )

    class Meta:
        model = User
        fields = '__all__'
