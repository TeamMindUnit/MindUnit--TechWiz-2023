from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # Add more fields as needed for patient information (e.g., address, contact)

    def __str__(self):
        return self.name

class HealthStatus(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    fever = models.CharField(max_length=10)
    cough = models.CharField(max_length=10)
    fatigue = models.CharField(max_length=10)
    difficulty_breathing = models.CharField(max_length=3)
    # Add more fields for other symptoms and health status data

    def __str__(self):
        return f"Health Status of {self.patient.name}"

class Prediction(models.Model):
    health_status = models.OneToOneField(HealthStatus, on_delete=models.CASCADE)
    prediction_result = models.CharField(max_length=100)
    prediction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction for {self.health_status.patient.name} on {self.prediction_date}"