from . import serializers
from taggit.models import Tag
from documents.models import Document
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class TagsViewSet(viewsets.ModelViewSet):

    
    queryset = Tag.objects.all()
    serializer_class = serializers.TagsSerializer
    permission_classes = [IsAuthenticated]