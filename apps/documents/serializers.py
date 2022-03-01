from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from rest_framework import serializers
from . models import Document

class DocumentSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Document
        fields = ['document_id', 'author', 'title', 'category', 'body', 'tags', 'created_date']