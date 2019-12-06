from django.db import models
# Create your models here.


class Meals(models.Model):
    id = models.IntegerField(primary_key=True)
    meal_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Meals'

    def __str__(self):
        return self.meal_name


class Recipes(models.Model):
    id = models.IntegerField(primary_key=True)
    recipe_name = models.CharField(max_length=200)
    recipe_category = models.ManyToManyField(Meals)

    class Meta:
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return self.recipe_name


class Ingredients(models.Model):
    id = models.IntegerField(primary_key=True)
    ingredient_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Ingredients'

    def __str__(self):
        return self.ingredient_name


class RecipeIngredients(models.Model):
    id = models.IntegerField(primary_key=True)
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    ingredient1 = models.ForeignKey(
        Ingredients, on_delete=models.CASCADE, related_name='ingredient1')
    quantity1 = models.CharField(max_length=100)
    ingredient2 = models.ForeignKey(
        Ingredients, on_delete=models.CASCADE, related_name='ingredient2')
    quantity2 = models.CharField(max_length=100)
    ingredient3 = models.ForeignKey(
        Ingredients, on_delete=models.CASCADE, related_name='ingredient3')
    quantity3 = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'RecipeIngredients'


class Directions(models.Model):
    id = models.IntegerField(primary_key=True)
    recipe_id = models.ForeignKey(
        Recipes, on_delete=models.SET_DEFAULT, default=1)
    directions = models.TextField()

    class Meta:
        verbose_name_plural = 'Directions'
