from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, Group
from django.contrib import admin
from django.utils.html import mark_safe


class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True,
                              help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")
    avatar = models.ImageField(
        upload_to='avatars/%Y/%m/%d/', default=None, null=True, blank=True, help_text="Upload avatar of the user")
    reset_code = models.IntegerField(null=True, blank=True)
    role = models.ForeignKey(
        Group, on_delete=models.SET_NULL, null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='users')

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "last_name", "first_name"]

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    @admin.display(description="Preview")
    def avatar_preview(self):
        if self.avatar:
            return mark_safe(f'<img src="{self.avatar.url}" alt="{self.username}" width="80" height="80" class="img-thumbnail rounded-circle shadow" />')
        return "No avatar"

    class Meta:
        ordering = ["id"]
