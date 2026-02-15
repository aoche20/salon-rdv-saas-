from rest_framework.routers import DefaultRouter
from .views import SalonViewSet, ServiceViewSet

router = DefaultRouter()
router.register("salons", SalonViewSet, basename="salon")
router.register("services", ServiceViewSet, basename="service")

urlpatterns = router.urls
