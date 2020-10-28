from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import  static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home),
    path('minfo1/', views.newinfo),
    path('minfo/', views.info),
    path('mexp/', views.experience),
    path('msalary/', views.salary),
    path('mleave/', views.leave),
    path('mlogin/', views.login),
    path('mdelete/', views.delete),
    path('cpass/',views.change),

]