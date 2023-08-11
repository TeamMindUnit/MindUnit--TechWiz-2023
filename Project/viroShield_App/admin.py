from django.contrib import admin
from .models.patients import Patient
from .models.predictions import Prediction
from .models.healthstatus import HealthStatus
# Register your models here.

admin.site.register(Patient)
admin.site.register(Prediction)
admin.site.register(HealthStatus)
