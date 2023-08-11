from django.db import models

from .patients import Patient


class HealthStatus(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    fever = models.CharField(max_length=10)
    cough = models.CharField(max_length=10)
    fatigue = models.CharField(max_length=10)
    difficulty_breathing = models.CharField(max_length=3)

    def __str__(self):
        return f"Health Status of {self.patient.name}"