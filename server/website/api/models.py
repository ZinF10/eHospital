from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, Group
from django.contrib import admin
from django.utils.html import mark_safe
from mdeditor.fields import MDTextField


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


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True, verbose_name="Active",
                                    help_text="Designates whether this object should be treated as active. Unselect this instead of deleting objects.")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["id"]


class ItemModel(BaseModel):
    slug = models.SlugField(default="", null=False, verbose_name="URL",
                            help_text="A short label, generally used in URLs.")

    class Meta(BaseModel.Meta):
        abstract = True
        ordering = BaseModel.Meta.ordering + ["slug"]


class Category(ItemModel):
    name = models.CharField(max_length=80, unique=True)
    description = MDTextField(null=True, blank=True)

    class Meta(ItemModel.Meta):
        ordering = ItemModel.Meta.ordering
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        ordering = BaseModel.Meta.ordering + ["name"]


class CommonModel(models.Model):
    tags = models.ManyToManyField(Tag)

    class Meta:
        abstract = True
        ordering = ["id"]


class Medication(ItemModel, CommonModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = MDTextField(null=True, blank=True)
    price = models.FloatField(default=0.00)

    class Meta(ItemModel.Meta):
        ordering = ItemModel.Meta.ordering + ["price"]

    def __str__(self):
        return self.name
