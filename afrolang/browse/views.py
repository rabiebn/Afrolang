from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def alpha(char):
    """Look-up slangs by Alphabetical order"""
    # the URL should look something like this: /browse?character=<A-Z>
    # Lookup all slangs starting with the char specified in the URL
    HttpRequest.GET('character')
    return HttpResponse("")

def date(date):
    """Look-up slangs by date url: /browse?date=YYYY-MM-DD"""
    
    return
