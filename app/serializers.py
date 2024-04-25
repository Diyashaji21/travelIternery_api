from rest_framework import serializers
from .models import ItineraryItem

class ItineraryItemSerializer(serializers.ModelSerializer):
    # Define a custom field for budget with predefined choices
    budget_choices = ['1000.00-5000.00', '5000.00-10000.00', '10000.00-1500.00', '15000.00-20000.00']  # Example choices
    budget = serializers.ChoiceField(choices=budget_choices)

    class Meta:
        model = ItineraryItem
        fields = ['id', 'destination', 'arrival_date', 'departure_date', 'transportation', 'budget']
