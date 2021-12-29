from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    """User main page"""
    return HttpResponse("User")


def profile(request):
    """User profile page"""
    return HttpResponse("User Profile")