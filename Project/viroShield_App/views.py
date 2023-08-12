from django.shortcuts import render
from .models import Patient, HealthStatus, Prediction

def home(request): 
    return render(request, 'home.html')

def symptoms_checker(request):
    if request.method == 'POST':
        # Get form data from POST request
        fever = request.POST.get('fever')
        cough = request.POST.get('cough')
        fatigue = request.POST.get('fatigue')
        difficulty_breathing = request.POST.get('difficultyBreathing')

        # Create HealthStatus instance
        patient = Patient.objects.create(name="John Doe", age=30, gender="M")
        health_status = HealthStatus.objects.create(patient=patient, fever=fever, cough=cough, fatigue=fatigue, difficulty_breathing=difficulty_breathing)

        # Perform prediction based on health_status and store the result
        # prediction_result = perform_prediction(health_status)
        prediction_result = "Potential viral infection"  # Replace with actual prediction

        Prediction.objects.create(health_status=health_status, prediction_result=prediction_result)

        context = {'prediction_result': prediction_result}
        return render(request, 'viroshield/index.html', context)

    return render(request, 'viroshield/index.html')


def dashboard(request):
    return render(request, 'admin/dashboard.html')
