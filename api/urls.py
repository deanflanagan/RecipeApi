
# from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import  RecipeViewSet, IngredientViewSet
 
router = routers.DefaultRouter()
router.register('ingredients', IngredientViewSet)
router.register('recipes', RecipeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
