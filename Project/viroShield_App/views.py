from django.shortcuts import render
from .models import Patient, HealthStatus, Prediction
import sweetviz as sv
from autoviz.AutoViz_Class import AutoViz_Class
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout


def home(request): 
    return render(request, 'home.html')

def perform_prediction(health_status):
    if health_status.fever == 'high' and health_status.cough == 'severe':
        return "Likely to have the flu"
    elif health_status.fever == 'low' and health_status.cough == 'wet' and health_status.fatigue == 'severe':
        return "Likely to have the flu"
    else:
        return "Unlikely to have the flu"

def symptoms_checker(request):
    if request.method == 'POST':
        # Get form data from POST request
        fever = request.POST.get('fever')
        cough = request.POST.get('cough')
        fatigue = request.POST.get('fatigue')
        difficulty_breathing = request.POST.get('difficultyBreathing')

        # Check if any symptom is not selected
        if fever == 'none' or cough == 'none' or fatigue == 'none' or difficulty_breathing == 'none':
            prediction_result = "Select all options"
        else:
            # Create HealthStatus instance
            patient = Patient.objects.create(name="John Doe", age=30, gender="M")
            health_status = HealthStatus.objects.create(patient=patient, fever=fever, cough=cough, fatigue=fatigue, difficulty_breathing=difficulty_breathing)

            # Perform prediction based on health_status and store the result
            prediction_result = perform_prediction(health_status)

            Prediction.objects.create(health_status=health_status, prediction_result=prediction_result)

        context = {'prediction_result': prediction_result}
        return render(request, 'viroshield/index.html', context)

    return render(request, 'viroshield/index.html')

@login_required
def dashboard(request):
    return render(request, 'admin/dashboard.html')

def register(request):
    if  request.method == 'GET':
        return render(request, 'admin/register.html')
    
    else:
        postData = request.POST
        f_name = postData.get('fname')
        l_name = postData.get('lname')
        email = postData.get('email')
        phone = postData.get('phone')
        password = postData.get('password')

        value = {
            'firstName': f_name,
            'lastName': l_name,
            'email':email,
            'password':password,
            'phoneno':phone,
        }
        myuser = User(first_name=f_name, last_name=l_name, email=email, phone_no=phone, password=password)

        error_msg = None

        if(not f_name):
            error_msg = 'First Name Required'
        elif len(f_name)> 30:
            error_msg = 'First Name cannot be less than 3 characters'

        if(not l_name):
            error_msg = 'Last Name Required'
        elif len (l_name)> 30:
            error_msg = 'Last Name cannot be less than 3 characters'

        if(not phone):
            error_msg = 'Phone Required'
        elif len (phone)> 11:
            error_msg = 'Phone Name cannot be less than 11 characters'

        if(not email):
            error_msg = 'Email Required'
        
        elif myuser.isExist():
            error_msg = 'Email already exist'


        if(not password):
            error_msg = 'Password Required'
        elif len (password)> 11:
            error_msg = 'Password Name cannot be less than 8 characters'

        if(not  error_msg):
            myuser.password = make_password(myuser.password)
            myuser.register()
            return redirect('productIndex')

        else:
            data = {
                'error': error_msg,
                'values': value
            }
        
        return render(request, 'register.html', data)

def logout_view(request):
    logout(request)
    return redirect('/') 

# datasheetURL = "E:/Ah2101a/ViroShield - Techwiz'23/flunet_dataset.xlsx"
datasheetURL = "../flunet_dataset.xlsx"

def sweetviz_report(request):

    df = pd.read_excel(datasheetURL)
    # df.iteritems = df.items
    report = sv.analyze(df)
    report.show_html('report.html') 

    context = {'report_path': 'report.html'}
    return render(request, 'admin/sweetviz_report.html', context)

def autoviz_report(request):
    df = pd.read_excel(datasheetURL)
    AV = AutoViz_Class()
    AV_report = AV.AutoViz(df)
    return render(request, 'admin/autoviz_report.html')