from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import  static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home),
    path('uleave/', views.leave),
    path('uattendance/', views.attendance),
    path('usalary/', views.salary),
    path('upass/',views.uchange),
    path('addinfo/',views.addinfo),
    path('academic/', views.academic),
    path('workexp/', views.workexp),
    path('workshopa/', views.workshopa),
    path('workshopo/',views.workshopo),
    path('achievements/', views.achievements),
    path('certifications/', views.certifications),
    path('strengths/', views.strengths),
    path('weakness/',views.weakness),
    path('workshopaw/', views.workshopaw),
    path('workshopac/', views.workshopac),
    path('workshopaf/', views.workshopaf),
    
]