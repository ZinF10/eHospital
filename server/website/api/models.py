from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, Group
from django.contrib import admin
from django.utils.html import mark_safe
from django.template.defaultfilters import slugify
from mdeditor.fields import MDTextField


class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True,
                              help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")
    avatar = models.ImageField(
        upload_to='avatars/%Y/%m/%d/', default=None, null=True, blank=True, help_text="Upload avatar of the user")
    reset_code = models.CharField(
        max_length=7, null=True, blank=True, unique=True)
    role = models.ForeignKey(
        Group, on_delete=models.SET_NULL, null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='users')

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "last_name", "first_name"]

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"

    def __str__(self):
        return self.get_full_name()

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    @admin.display(description="Preview")
    def avatar_preview(self):
        if self.avatar:
            return mark_safe(f'<img src="{self.avatar.url}" alt="{self.username}" width="80" height="80" class="img-thumbnail rounded-circle shadow" />')

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
                            help_text="A short label, generally used in URLs.", unique=True)

    class Meta(BaseModel.Meta):
        abstract = True
        ordering = BaseModel.Meta.ordering + ["slug"]


class InforModel(ItemModel):
    phone = models.CharField(max_length=20, null=True, blank=True)

    class Meta(BaseModel.Meta):
        abstract = True
        ordering = ItemModel.Meta.ordering + ['phone']


class Patient(InforModel):
    BLOOD_GROUP = (
        ("A-", "A-"),
        ("A+", "A+"),
        ("B-", "B-"),
        ("B+", "B+"),
        ("AB-", "AB-"),
        ("AB+", "AB+"),
        ("O-", "O-"),
        ("O+", "O+"),
        ("NS", "Not Set"),
    )
    GENDER_TYPE = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_group = models.CharField(
        max_length=5,
        default="NS",
        choices=BLOOD_GROUP
    )
    gender = models.CharField(
        max_length=1, choices=GENDER_TYPE, default='O')
    location = models.CharField(max_length=125, null=True, blank=True)
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        help_text="Please use the following format: <em>YYYY-MM-DD</em>."
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)

    class Meta(InforModel.Meta):
        ordering = InforModel.Meta.ordering + ['user']

    def __str__(self):
        return self.user.get_full_name()


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


class Department(ItemModel):
    name = models.CharField(max_length=80, unique=True)
    description = MDTextField(null=True, blank=True)

    class Meta(ItemModel.Meta):
        ordering = ItemModel.Meta.ordering

    def __str__(self):
        return self.name


class Doctor(InforModel, CommonModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = MDTextField(null=True, blank=True)
    price = models.FloatField(default=0.00)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)

    class Meta(InforModel.Meta):
        ordering = InforModel.Meta.ordering + ['user']

    def __str__(self):
        return self.user.get_full_name()


class Experience(BaseModel):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hospital = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    start_date = models.DateField("From")
    end_date = models.DateField("To", blank=True)
    description = MDTextField(null=True, blank=True)

    def __str__(self):
        return f"{self.designation} {self.hospital}"

    class Meta:
        ordering = ["id"]


class Award(BaseModel):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date_received = models.DateField()
    description = MDTextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} {self.date_received}"

    class Meta:
        ordering = BaseModel.Meta.ordering + ["-date_received"]


class Nurse(InforModel, CommonModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.get_full_name()


class Category(ItemModel):
    name = models.CharField(max_length=80, unique=True)
    description = MDTextField(null=True, blank=True)

    class Meta(ItemModel.Meta):
        ordering = ItemModel.Meta.ordering
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Medication(ItemModel, CommonModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = MDTextField(null=True, blank=True)
    price = models.FloatField(default=0.00)
    image = models.ImageField(upload_to='medications/%Y/%m/%d/',
                              blank=True, help_text="Upload image of the medication")

    class Meta(ItemModel.Meta):
        ordering = ItemModel.Meta.ordering + ["price"]

    def __str__(self):
        return self.name
