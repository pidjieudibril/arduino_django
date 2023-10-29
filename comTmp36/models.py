# models.py
from django.db import models
from django.utils import timezone

class TemperatureData(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.temperature} , {self.timestamp}'