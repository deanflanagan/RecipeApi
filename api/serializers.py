from rest_framework import serializers
from .models import Recipe,  Ingredient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id','name', 'meat']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
   
    class Meta:
        model = Recipe
        fields = ['id','title','quick', 'ingredients'] #,'user'

    def create(self, validated_data):
        ingredients = [Ingredient(**item) for item in validated_data.pop('ingredients')] # has to be a min of 2 ingredients
        if len(ingredients) < 2:
            print('You need more ingredients than that')
            return 
        else:
            for ing in ingredients:
                try:
                    res = Ingredient.objects.get(name=ing.name)
                except:
                    ing.save()
            recipe = Recipe.objects.create(**validated_data)
            return recipe

 
class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = User 
        fields = ['id','username', 'password']
        extra_kwargs = {'password':{'write_only':True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user