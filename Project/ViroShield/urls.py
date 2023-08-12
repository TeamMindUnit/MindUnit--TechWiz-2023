from django.contrib import admin
from django.urls import path
from viroShield_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = "home"),
    path('symptoms_checker/', views.symptoms_checker, name='symptoms_checker'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
