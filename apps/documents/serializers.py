from os import read
from unicodedata import category
from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from rest_framework import serializers
from . models import Document

class DocumentSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    document_id = serializers.CharField(allow_blank=True)
    category_name = serializers.CharField(source="category.name", read_only=True)
    class Meta:
        model = Document
        fields = ['document_id', 'author', 'title', 'category', 'category_name', 'body', 'tags', 'created_date']
        read_only_fields = ['created_date']
