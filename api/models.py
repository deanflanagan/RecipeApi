#from django.core.validators import  MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=32)
    meat = models.BooleanField(default=False)

    def __str__(self):
        return self.name 
    
class Recipe(models.Model):
    title = models.CharField(max_length=32, blank=False)
    quick = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, related_name='ingredients')#,validators=[MinValueValidator(2)])

    # @action(detail=True, methods=['POST'])
    # def 
       

    def __str__(self):
        return self.title
    
