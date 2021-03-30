from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dinner(models.Model):
    day = models.DateField()

    def __str__(self):
        return self.day
    
class Recipe(models.Model):
    title = models.CharField(max_length=32, blank=False)
    quick = models.BooleanField()
    dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, related_name='recipes')
    

    def __str__(self):
        return self.title
    
class Ingredient(models.Model):
    ingredient = models.CharField(max_length=32)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient 