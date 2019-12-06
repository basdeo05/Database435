from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import RecipeIngredients, Recipes, Directions, Ingredients, Meals
# Create your views here.


class CreateRecipe(object):
    recipe_name = ''
    ingredients = []
    directions = []

    def __init__(self, name, ings, dirs):
        self.recipe_name = name
        self.ingredients = ings
        self.directions = dirs


def objectify(query_set):

    recipes = []

    for i in query_set:
        name = str(i.recipe_id)
        ings = [f"{i.quantity1} {str(i.ingredient1)}", f"{i.quantity2} {str(i.ingredient2)}",
                f"{i.quantity3} {str(i.ingredient3)}"]
        d = Directions.objects.filter(recipe_id=i.recipe_id)
        dirs = [i.directions for i in d]
        r = CreateRecipe(name, ings, dirs)
        recipes.append(r)

    return recipes


def homepage(request):
    return render(request, template_name='website/home.html')


def search(request):

    query = request.GET.get('q')

    if query:
        results = RecipeIngredients.objects.filter(
            Q(recipe_id__recipe_name__icontains=query) |
            Q(ingredient1__icontains=query) |
            Q(ingredient2__icontains=query) |
            Q(ingredient3__icontains=query)
        ).distinct()

        results = objectify(results)
        return render(request, template_name='website/results.html', context={'results': results})


def categories(request):
    meals = Meals.objects.all()  # get all categories
    # return meals to categories.html
    return render(request, template_name='website/results.html', context={'meals': meals})


def recipes(request, meal_name):
    meals = [m.meal_name for m in Meals.objects.all()]
    if meal_name in meals:
        recipe_names = Recipes.objects.filter(
            recipe_category__meal_name=meal_name)
        print(meal_name)
        return render(request, template_name='website/recipes.html', context={'recipes': recipe_names})

    r = [r.recipe_name for r in Recipes.objects.all()]
    if meal_name in r:
        recipe = RecipeIngredients.objects.filter(
            recipe_id__recipe_name=meal_name)
        r2 = objectify(recipe)
        return render(request, template_name='website/meals.html', context={'r2': r2})

    return HttpResponse("there's no data that matches")
