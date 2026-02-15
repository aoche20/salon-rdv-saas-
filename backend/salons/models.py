from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Salon(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salons')
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    price_fcfa = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.price_fcfa} FCFA"


class Employee(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name='employees')
    name = models.CharField(max_length=100)
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.name
