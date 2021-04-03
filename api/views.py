from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action 
from django.contrib.auth.models import User
from .models import  Recipe, Ingredient
from .serializers import  RecipeSerializer, IngredientSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    @action(detail=True, methods=['POST'])
    def adjust_recipe(self, request, pk=None):
        if 'ingredients' in request.data :
            recipe = Recipe.objects.get(id=pk)
            user = User.objects.get(id=1)

            for ing in recipe.ingredients.all():
                print(ing.name)
            # 1 check if there's already ingredietns in there. If not, we create. If yes, we update.
            # try:
            #     current_ingredients = recipe.ingredients.all()



            response = {'message':'its working'}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message':'You need to provide at least two ingredients'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)           

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer