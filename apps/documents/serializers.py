from unicodedata import category
from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from rest_framework import serializers
from . models import Document

class DocumentSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    category_name = serializers.CharField(source="category.name")
    class Meta:
        model = Document
        fields = ['document_id', 'author', 'title', 'category', 'category_name',  'body', 'tags', 'created_date']