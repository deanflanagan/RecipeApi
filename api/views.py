from rest_framework import viewsets
from .models import Dinner, Recipe, Ingredient
from .serializers import DinnerSerializer, RecipeSerializer, IngredientSerializer
# Create your views here.


class DinnerViewSet(viewsets.ModelViewSet):
    queryset = Dinner.objects.all()
    serializer_class = DinnerSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer