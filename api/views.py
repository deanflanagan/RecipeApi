from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action 
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from .models import  Recipe, Ingredient
from .serializers import  RecipeSerializer, IngredientSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    authentication_classes = (TokenAuthentication,)

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    authentication_classes = (TokenAuthentication,)
