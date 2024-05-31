"""
URL configuration for home app.
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.alpha, name='browse-alpha'),
    path('', views.date, name='browse-date'),
]
