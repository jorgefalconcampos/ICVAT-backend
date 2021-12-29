from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """User main page"""
    return HttpResponse("User main")

def profile(request):
    """Profile main page"""
    return HttpResponse("User Profile")
