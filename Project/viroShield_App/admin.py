from django.contrib import admin
from .models.patients import Patient
from .models.predictions import Prediction
from .models.healthstatus import HealthStatus
from .models.user import User

admin.site.register(Patient)
admin.site.register(Prediction)
admin.site.register(HealthStatus)
admin.site.register(User)