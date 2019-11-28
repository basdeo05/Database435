from django.contrib import admin
from .models import Meals, Ingredients, Recipes, RecipeIngredients, Directions

# Register your models here.
admin.site.register(Meals)
admin.site.register(Ingredients)
admin.site.register(Recipes)
admin.site.register(RecipeIngredients)
admin.site.register(Directions)
