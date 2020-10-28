from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import  static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('about/', views.about),
    path('portfolio/', views.portfolio),
    path('contact/', views.contact),
    path('projectengg/',views.engineering),
    path('projectmanage/',views.management),
    path('projectcom/',views.commerce),
    path('projectscience/',views.science),
    path('projectsocial/',views.social),
    path('projectart/',views.art),
    path('projecthuman/',views.human),
    path('projectpharm/',views.pharmacy),
    path('projectagri/',views.agriculture),
    path('ad94bHry73/', include('ad94bHry73.urls')),
    path('mahd748hdYd/', include('mahd748hdYd.urls')),
    path('uy43hBgd843/', include('uy43hBgd843.urls')),
    path('forget/',views.forget),

    
]
