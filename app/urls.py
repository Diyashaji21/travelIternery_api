from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItineraryItemViewSet

router = DefaultRouter()
router.register(r'itinerary-items', ItineraryItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]