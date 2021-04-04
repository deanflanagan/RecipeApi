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
        recipe = Recipe.objects.create(user=self.context['request'].user, quick=validated_data['quick'], title=validated_data['title'])
        recipe.save()
        ingredients = [Ingredient(**item) for item in validated_data.pop('ingredients')] # has to be a min of 2 ingredients
        # here validate the ingredients and first make the recipe. Then add or set them one by one.
        for ing in ingredients:
            try:
                ing = Ingredient.objects.get(name=ing.name) # if this throws an error it will make a new ingredient
            except:
                ing.save()
            recipe.ingredients.add(ing)
            print(recipe)
        return recipe

 
class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = User 
        fields = ['id','username', 'password']
        extra_kwargs = {'password':{'write_only':True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user