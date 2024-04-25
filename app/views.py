from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import ItineraryItem
from .serializers import ItineraryItemSerializer
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

def validate_arrival_date_before_departure(value):
    if value['arrival_date'] >= value['departure_date']:
        raise ValidationError(
            _('Arrival date should be before departure date')
        )
    

class ItineraryItemViewSet(viewsets.ModelViewSet):
    queryset = ItineraryItem.objects.all()
    serializer_class = ItineraryItemSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        itinerary_item = self.get_object()
        serializer = self.get_serializer(itinerary_item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        itinerary_item = self.get_object()
        itinerary_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def clean(self):
        validate_arrival_date_before_departure({'arrival_date': self.arrival_date, 'departure_date': self.departure_date})