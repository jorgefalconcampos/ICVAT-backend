from rest_framework.validators import UniqueValidator
from rest_framework.response import Response
from rest_framework import serializers
from . models import Category

from django.db.models.functions import Lower


class CategorySerializer(serializers.ModelSerializer):

    def validate(self, data):
        owner = data.get("owner").id
        name = data.get("name")

        
        print(name)
        # print(data.get("owner").id)
        if not (Category.objects.filter(owner=owner, name=name)):
            print("no existe, puedes crearla")
        else:
            print("esta catego ya existe para este usuario")
            raise serializers.ValidationError("This category already exists")
        # if (Category.objects.filter(owner=owner, name)):
            # print("este usuario ya tiene una catego con este nombre")


        return data

    # def create(self, attrs):

        # if (attrs.get("owner").id):
        #     print("si hay")

        # name = attrs.get("name")

        # if (Category.objects.filter(name=name).first()):
        #     raise serializers.ValidationError("Already exist")
        # else:
        #     print("otro")

        

        # return super().validate(attrs)    
    # user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())


    # name = serializers.CharField(
    #     validators=[UniqueValidator(
    #         queryset=Category.objects.filter(owner=user), message="This category already exists"
    #     )])

    
    class Meta:
        model = Category
        
        # fields = "__all__"
        fields = ['id', 'name', 'owner', 'description', 'slug']



    