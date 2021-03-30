from rest_framework import serializers
from .models import Recipe,  Ingredient

class RecipeSerializer(serializers.ModelSerializer):
    
    # ingredients = IngredientSerializer(many=True)
    class Meta:
        model = Recipe
        fields = ['title','quick', 'ingredients']


class IngredientSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True)
    class Meta:
        model = Ingredient
        fields = ['ingredient']



# class DinnerSerializer(serializers.ModelSerializer):
#     recipes = RecipeSerializer(many=True)
#     class Meta:
#         model = Dinner
#         fields = ['day', 'recipes']