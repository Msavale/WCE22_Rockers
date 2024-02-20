from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path("", views.accounts, name="accounts"),
    path("inwardRemitance/", views.inwardRemitance, name="inwardRemitance"),
    path("inwardRemitanceTable/", views.inwardRemitanceTable, name="inwardRemitanceTable"),
    path("brc/", views.brc, name="brc"),
    path("brcTable/", views.brcTable, name="brcTable"),
    path("docBank/", views.docBank, name="docSubmissionToBank"),
    path("docBankTable/", views.docBankTable, name="docBankTable"),
    path("billOceanTptCha/", views.billOceanTptCha, name="billForOceanTptCha"),
    path("billOceanTptChaTable/", views.billOceanTptChaTable, name="billOceanTptChaTable")
]