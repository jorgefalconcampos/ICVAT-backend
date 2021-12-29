from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def categories(request):
    """Categories main page"""
    return HttpResponse("Categories")


def add(request):
    """Categories add"""
    return HttpResponse("Add Category")


def edit(request):
    """Categories edit"""
    return HttpResponse("Edit Category")


def delete(request):
    """Categories delete"""
    return HttpResponse("Delete Category")