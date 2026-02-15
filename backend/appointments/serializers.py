from rest_framework import serializers
from .models import Appointment
from .services import is_slot_available

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

    def validate(self, data):
        if not is_slot_available(
            data['employee'],
            data['date'],
            data['start_time'],
            data['end_time']
        ):
            raise serializers.ValidationError(
                "Ce créneau n’est plus disponible"
            )
        return data