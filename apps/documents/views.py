from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    """Documents main page"""
    return HttpResponse("Documents")


def add(request):
    """Documents add"""
    return HttpResponse("Add document")


def edit(request):
    """Documents edit"""
    return HttpResponse("Edit document")


def delete(request):
    """Documents delete"""
    return HttpResponse("Delete document")