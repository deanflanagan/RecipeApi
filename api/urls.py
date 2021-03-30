
# from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import DinnerViewSet, RecipeViewSet, IngredientViewSet
 
router = routers.DefaultRouter()
router.register('dinners', DinnerViewSet)
router.register('ingredients', IngredientViewSet)
router.register('recipes', RecipeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
