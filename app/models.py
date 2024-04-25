from django.db import models

class ItineraryItem(models.Model):
    TRANSPORTATION_CHOICES = [
        ('car', 'Car'),
        ('bus', 'Bus'),
        ('train', 'Train'),
        ('flight', 'Flight'),
    ]

    BUDGET_CHOICES = [
        (1000, '1000 - 2000'),
        (2000, '2000 - 3000'),
        (3000, '3000 - 4000'),
        (4000, '4000 - 5000'),
        # Add more ranges as needed
    ]

    destination = models.CharField(max_length=100)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    transportation = models.CharField(max_length=100, choices=TRANSPORTATION_CHOICES)
    budget = models.CharField(max_length=100, choices=BUDGET_CHOICES)

    def __str__(self):
        return f"{self.destination} ({self.arrival_date} to {self.departure_date})"
