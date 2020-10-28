from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import  static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home),
    path('mlapplicants/', views.applicants),
    path('mlattendance/', views.attendance),
    path('mlapproval/', views.approval),
    path('mpass/',views.mchange),
    path('search/',views.search),

]