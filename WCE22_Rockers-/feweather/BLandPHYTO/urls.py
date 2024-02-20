from django.contrib import admin
from django.urls import path
from BLandPHYTO import views

urlpatterns = [
    path("", views.blAndPhytoUpdate, name="blAndPhytoUpdate"),
    path("", views.blAndPhytoView, name="blAndPhytoView"),
]