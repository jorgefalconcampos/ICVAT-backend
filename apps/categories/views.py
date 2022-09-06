from rest_framework.permissions import IsAuthenticated
from . permissions import IsOwner
from . import serializers
from . models import Category
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.db.models.functions import Lower


class CategoryViewSet(viewsets.ModelViewSet):
    # queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    # authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user).order_by(Lower('slug').asc())




def categories(request):
    """Categories main page"""
    return HttpResponse("Categories")


def add(request):
    """Categories add"""
    return HttpResponse("Add Category")

def static(request):
    template = 'categories/index.html'
    return render(request, template, {})

def edit(request):
    """Categories edit"""
    return HttpResponse("Edit Category")


def delete(request):
    """Categories delete"""
    return HttpResponse("Delete Category")