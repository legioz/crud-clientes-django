from django.db import models
from apps.core import managers
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    birth = models.DateField("Birth Date", blank=False, null=True)
    is_active = models.BooleanField("Active", default=True, blank=False, null=False)
    is_staff = models.BooleanField("Staff", default=False, blank=False, null=False)
    is_superuser = models.BooleanField(
        "Superuser", default=False, blank=False, null=False
    )
    is_deleted = models.BooleanField("Deleted", default=False, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    username = None
    objects = managers.UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"

    def get_username(self):
        return self.email

    def __str__(self) -> str:
        return self.email
