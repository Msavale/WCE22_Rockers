from django.contrib import admin
from django.urls import path
from EGM_Status import views

urlpatterns = [
    path("", views.egmView, name="egm_view"),
    path("", views.egmUpdate, name="egm_update"),
    path("", views.egmInfo, name="egm_info"),
]