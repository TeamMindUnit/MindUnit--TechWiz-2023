from django.db import models

from .healthstatus import HealthStatus


class Prediction(models.Model):
    health_status = models.OneToOneField(HealthStatus, on_delete=models.CASCADE)
    prediction_result = models.CharField(max_length=100)
    prediction_date = models.DateTimeField(auto_now_add=True)

    @property
    def __str__(self):
        return f"Prediction for {self.health_status.patient.name} on {self.prediction_date}"