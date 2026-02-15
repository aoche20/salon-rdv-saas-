from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AppointmentViewSet, AvailableSlotsView

router = DefaultRouter()
router.register(r"appointments", AppointmentViewSet, basename="appointment")

urlpatterns = [
    path("available-slots/", AvailableSlotsView.as_view(), name="available-slots"),
]

urlpatterns += router.urls
