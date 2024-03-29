from rest_framework.validators import UniqueValidator
from rest_framework.response import Response
from django.db.models.functions import Lower
from rest_framework import serializers
from . models import Category



class CategorySerializer(serializers.ModelSerializer):

    def validate(self, data):
        if (self.context.get('request').method == 'POST'):
            owner = data.get("owner").id
            name = data.get("name")
            if (Category.objects.filter(owner=owner, name__icontains=name)):
                raise serializers.ValidationError("Category name already exists")
            return data
        else:
            return data
    
    class Meta:
        model = Category
        # fields = "__all__"
        fields = ['id', 'name', 'owner', 'description', 'slug']



    