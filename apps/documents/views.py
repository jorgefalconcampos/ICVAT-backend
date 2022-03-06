from codecs import lookup
from rest_framework import generics

from apps.categories import permissions
from . import serializers
from . models import Document

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated



class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = serializers.DocumentSerializer
    lookup_field = "document_id"
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
        # return Document.objects.filter(author=self.request.user)

    


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