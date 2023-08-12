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

import sweetviz as sv
from autoviz.AutoViz_Class import AutoViz_Class
import pandas as pd

# def sweetviz_report(request):
#     df = pd.read_excel('E:/Ah2101a/ViroShield/flunet_dataset.xlsx')
#     df.iteritems = df.items
#     report = sv.analyze(df)
#     report.show_html('report.html')   
#     return render(request, 'admin/sweetviz_report.html')
def sweetviz_report(request):

    df = pd.read_excel('E:/Ah2101a/ViroShield/flunet_dataset.xlsx')
    # df.iteritems = df.items
    report = sv.analyze(df)
    report.show_html('report.html')  # This line generates the report HTML

    # Pass the report file path to the template
    context = {'report_path': 'report.html'}
    return render(request, 'admin/sweetviz_report.html', context)

def autoviz_report(request):
    df = pd.read_excel('E:/Ah2101a/ViroShield/flunet_dataset.xlsx')
    AV = AutoViz_Class()
    AV_report = AV.AutoViz(df)
    return render(request, 'admin/autoviz_report.html')