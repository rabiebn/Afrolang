"""
Home App views
"""
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """Home Page"""
    return HttpResponse("<h1>Afrolang</h1>\n<h2>Home page</h2>")

