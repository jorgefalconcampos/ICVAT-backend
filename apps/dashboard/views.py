from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def dashboard(request):
    """Dashboard main page"""
    return HttpResponse("Dashboard")


def latest(request):
    """Dashboard latest page"""
    return HttpResponse("Dashboard latest")