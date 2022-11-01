from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('contact/',views.contactUs),
    path("about/",views.aboutUs)
]