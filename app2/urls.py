from django.contrib import admin
from django.urls import path
from app2 import views

urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("service", views.service, name='service')
]
