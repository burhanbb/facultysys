from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import  static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('about/', views.about),
    path('contact/', views.contact),
    path('ad94bHry73/', include('ad94bHry73.urls')),
    path('mahd748hdYd/', include('mahd748hdYd.urls')),
    path('uy43hBgd843/', include('uy43hBgd843.urls')),
    path('forget/',views.forget),

    
]
