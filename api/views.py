from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action 
from .models import  Recipe, Ingredient
from .serializers import  RecipeSerializer, IngredientSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    @action(detail=True, methods=['POST'])
    def add_ingredients(self, request, pk=None):
        print(pk)

        if 'ingredients' in request.data:
            recipe = Recipe.objects.get(id=pk)
            # print(dir(recipe))
            # print(recipe.ingredients)
            # print(recipe.title)

            response = {'message':'its working'}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message':'You need to provide at least two ingredients'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)           

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer