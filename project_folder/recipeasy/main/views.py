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
    #each item in the query_set is a row in the db table, we want to piece the data together
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
    return render(
        request, 
        template_name='website/home.html')


def search(request):
    #get the query string in request
    query = request.GET.get('q')

    if query:
        #if query string is not empty
        results = RecipeIngredients.objects.filter(
            Q(recipe_id__recipe_name__icontains=query) |
            Q(ingredient1__ingredient_name__icontains=query) |
            Q(ingredient2__ingredient_name__icontains=query) |
            Q(ingredient3__ingredient_name__icontains=query) |
            Q(recipe_id__recipe_category__meal_name__icontains=query)
        ).distinct()

        results = objectify(results)
        return render(
            request, 
            template_name='website/results.html', 
            context={'recipes': results, 'query':query})

    return render(
        request, 
        template_name='website/results.html', 
        context={'query':query})

    
def categories(request):
    # get all categories
    meals = Meals.objects.all()

    # return meals to categories.html
    return render(
        request, 
        template_name='website/categories.html', 
        context={'meals': meals})


def recipes(request, name):
    meals = [m.meal_name for m in Meals.objects.all()]
    #check if name is a meal
    if name in meals:
        recipe_names = Recipes.objects.filter(
            recipe_category__meal_name=name)
        return render(
            request, 
            template_name='website/recipelist.html', 
            context={'recipes': recipe_names, 'category': name})

    recipes = [r.recipe_name for r in Recipes.objects.all()]
    #check if name is a recipe
    if name in recipes:
        recipe = RecipeIngredients.objects.filter(
            recipe_id__recipe_name=name)
        #objectify converts matched recipes to class objects for easier access with html
        recipe = objectify(recipe)
        
        return render(
            request, 
            template_name='website/recipe.html', 
            context={'recipe': recipe})

    #if neither is true 
    return HttpResponse("There's no data that matches")

def about_us(request):
    return render(request,template_name='website/aboutus.html')
