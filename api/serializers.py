from rest_framework import serializers
from .models import Recipe, Dinner, Ingredient

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['title','quick', 'dinner']

class DinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dinner
        fields = ['day']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['ingredient', 'recipe', 'user']