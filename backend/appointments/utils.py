from datetime import datetime, timedelta

def generate_time_slots(start_time, end_time, duration_minutes):
    """
    Génère des créneaux [start, end) selon la durée du service
    """
    slots = []
    current = datetime.combine(datetime.today(), start_time)
    end_dt = datetime.combine(datetime.today(), end_time)

    while current + timedelta(minutes=duration_minutes) <= end_dt:
        slots.append((
            current.time(),
            (current + timedelta(minutes=duration_minutes)).time()
        ))
        current += timedelta(minutes=duration_minutes)

    return slots
