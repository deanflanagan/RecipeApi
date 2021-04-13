from rest_framework import serializers
from .models import Recipe,  Ingredient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'meat']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'quick', 'ingredients']  # ,'image'] #,'user'

    def create(self, validated_data):
        recipe = Recipe.objects.create(
            user=self.context['request'].user, quick=validated_data['quick'], title=validated_data['title'])
        recipe.save()
        # has to be a min of 2 ingredients on front end
        ingredients = [Ingredient(**item)
                       for item in validated_data.pop('ingredients')]
        for ingredient in ingredients:
            try:
                # if this throws an error it will make a new ingredient
                ingredient = Ingredient.objects.get(name=ingredient.name)
            except:
                ingredient.save()
            recipe.ingredients.add(ingredient)
        return recipe

    def update(self, instance, validated_data):

        ingredients_data = validated_data.pop('ingredients')
        instance.title = validated_data.get('title', instance.title)
        instance.quick = validated_data.get('quick', instance.quick)
        instance.save()

        for ingredient in ingredients_data:
            ingredient, created = Ingredient.objects.get_or_create(
                name=ingredient['name'])

            instance.ingredients.add(ingredient)

        return instance


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
