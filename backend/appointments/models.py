from django.db import models

# Create your models here.
class Availability(models.Model):
    employee = models.ForeignKey(
        'salons.Employee',
        on_delete=models.CASCADE,
        related_name='availabilities'
    )
    weekday = models.IntegerField(
        choices=[(i, day) for i, day in enumerate([
            'Lundi', 'Mardi', 'Mercredi', 'Jeudi',
            'Vendredi', 'Samedi', 'Dimanche'
        ])]
    )
    start_time = models.TimeField()
    end_time = models.TimeField()

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'En attente'),
        ('CONFIRMED', 'Confirmé'),
        ('CANCELED', 'Annulé'),
    )

    salon = models.ForeignKey('salons.Salon', on_delete=models.CASCADE)
    service = models.ForeignKey('salons.Service', on_delete=models.CASCADE)
    employee = models.ForeignKey('salons.Employee', on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=20)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('employee', 'date', 'start_time')

    def __str__(self):
        return f"{self.client_name} - {self.date} {self.start_time}"
