from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, IntegerField, EmailField, TextChoices


class User(AbstractUser):
    class Role(TextChoices):
        ADMIN = "admin", 'Admin'
        OPERATOR = "operator", 'Operator'
        MANAGER = "manager", 'Manager'
        DRIVER = "driver", 'Driver'
        USER = "user", 'User'

    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    phone_number = IntegerField()
    email = EmailField()
    role = CharField(max_length=255, choices=Role.USER, default=Role.USER)
