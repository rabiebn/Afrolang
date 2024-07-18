"""
Views for Definitions
"""
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """test"""
    return HttpResponse("A slang with its definition supposed to be here!")
