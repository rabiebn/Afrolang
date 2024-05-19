"""
URL configuration for home app.
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.browse, name='browse-page'),
]
