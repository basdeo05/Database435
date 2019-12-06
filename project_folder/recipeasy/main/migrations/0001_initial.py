# Generated by Django 2.2.7 on 2019-11-28 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ingredient_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('meal_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('recipe_name', models.CharField(max_length=200)),
                ('recipe_category', models.ManyToManyField(to='main.Meals')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredients',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity1', models.CharField(max_length=100)),
                ('quantity2', models.CharField(max_length=100)),
                ('quantity3', models.CharField(max_length=100)),
                ('ingredient1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient1', to='main.Ingredients')),
                ('ingredient2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient2', to='main.Ingredients')),
                ('ingredient3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient3', to='main.Ingredients')),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Recipes')),
            ],
        ),
        migrations.CreateModel(
            name='Directions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('directions', models.TextField()),
                ('recipe_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Recipes')),
            ],
        ),
    ]
