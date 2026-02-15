from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('OWNER', 'Propriétaire'),
        ('EMPLOYEE', 'Employé'),
        ('CLIENT', 'Client'),
    )

    phone_number = models.CharField(max_length=20, unique=True)
    fullname = models.CharField(max_length=100, blank=True) 
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='CLIENT')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()  # 🔥 LIGNE CRITIQUE

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number
