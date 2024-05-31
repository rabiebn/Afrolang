"""
Home App views
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from random import random


def home(request):
    """Home Page"""
    return HttpResponse("<h1>Afrolang</h1>\n<h2>Home page</h2>")

def hi(request):
    template = loader.get_template("../static/drafthi.html")
    return HttpResponse(template.render)

def randomizer(request):
    """Generates a list of random slangs upon visiting home page"""
    return