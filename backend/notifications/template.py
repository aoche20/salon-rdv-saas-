def appointment_confirmation(appointment):
    return (
        f"Bonjour {appointment.client_name},\n\n"
        f"Votre rendez-vous est confirmé ✅\n"
        f"📅 Date : {appointment.date}\n"
        f"⏰ Heure : {appointment.start_time.strftime('%H:%M')}\n"
        f"💇 Service : {appointment.service.name}\n"
        f"📍 Salon : {appointment.salon.name}\n\n"
        f"Merci et à bientôt 🙏"
    )


def appointment_reminder(appointment):
    return (
        f"⏰ Rappel rendez-vous\n\n"
        f"Bonjour {appointment.client_name},\n"
        f"Votre rendez-vous est prévu aujourd’hui à "
        f"{appointment.start_time.strftime('%H:%M')}.\n\n"
        f"À tout à l’heure !"
    )
