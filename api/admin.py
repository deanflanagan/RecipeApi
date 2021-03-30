from django.contrib import admin
from .models import Recipe, Dinner,Ingredient

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Dinner)
admin.site.register(Ingredient)
