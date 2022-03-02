from rest_framework.validators import UniqueValidator
from rest_framework.response import Response
from rest_framework import serializers
from . models import Category

from django.db.models.functions import Lower


class CategorySerializer(serializers.ModelSerializer):

    def validate(self, data):
        owner = data.get("owner").id
        name = data.get("name")
        if (Category.objects.filter(owner=owner, name=name)):
            raise serializers.ValidationError("Category name already exists")
        return data
    
    class Meta:
        model = Category
        # fields = "__all__"
        fields = ['id', 'name', 'owner', 'description', 'slug']



    