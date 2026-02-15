from datetime import datetime

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import ValidationError, NotFound
from notifications.whatsapp import send_whatsapp_message
from notifications.template import appointment_confirmation

from .models import Appointment, Availability
from .serializers import AppointmentSerializer
from .utils import generate_time_slots
from .services import is_slot_available

from salons.models import Employee, Service

class AppointmentViewSet(ModelViewSet):
    """
    CRUD des rendez-vous pour le propriétaire du salon
    """
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Appointment.objects.filter(
            salon__owner=self.request.user
        ).order_by("-created_at")
    
    @action(detail=True, methods=["patch"])
    def status(self, request, pk=None):
        appointment = self.get_object()
        appointment.status = request.data["status"]
        appointment.save()
        return Response({"status": appointment.status})
    
    def perform_create(self, serializer):
        appointment = serializer.save()

        # Envoi WhatsApp confirmation
        message = appointment_confirmation(appointment)
        send_whatsapp_message(
            appointment.client_phone,
            message
        )
class AvailableSlotsView(APIView):
    """
    Retourne les créneaux disponibles pour :
    - un employé
    - un service
    - une date donnée
    """
    permission_classes = [AllowAny]

    def get(self, request):
        employee_id = request.query_params.get("employee")
        service_id = request.query_params.get("service")
        date_str = request.query_params.get("date")

        # 1️⃣ Validation paramètres
        if not all([employee_id, service_id, date_str]):
            raise ValidationError(
                "Paramètres requis : employee, service, date (YYYY-MM-DD)"
            )

        # 2️⃣ Récupération objets
        try:
            employee = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            raise NotFound("Employé introuvable")

        try:
            service = Service.objects.get(id=service_id)
        except Service.DoesNotExist:
            raise NotFound("Service introuvable")

        # 3️⃣ Parsing date
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValidationError("Format date invalide (YYYY-MM-DD)")

        weekday = date.weekday()

        # 4️⃣ Disponibilités employé
        availabilities = Availability.objects.filter(
            employee=employee,
            weekday=weekday
        )

        available_slots = []

        # 5️⃣ Génération créneaux
        for availability in availabilities:
            slots = generate_time_slots(
                availability.start_time,
                availability.end_time,
                service.duration_minutes
            )

            for start, end in slots:
                if is_slot_available(employee, date, start, end):
                    available_slots.append({
                        "start": start.strftime("%H:%M"),
                        "end": end.strftime("%H:%M")
                    })

        return Response({
            "employee": employee.id,
            "service": service.id,
            "date": date_str,
            "slots": available_slots
        })
