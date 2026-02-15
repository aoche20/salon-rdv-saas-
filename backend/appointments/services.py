from .models import Appointment

def is_slot_available(employee, date, start_time, end_time):
    return not Appointment.objects.filter(
        employee=employee,
        date=date,
        start_time__lt=end_time,
        end_time__gt=start_time,
        status__in=['PENDING', 'CONFIRMED']
    ).exists()
