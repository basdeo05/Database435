from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('categories/', views.categories, name='search'),
    path('search/', views.search, name='search'),
    path('categories/<name>', views.recipes, name='meal_name'),
    path('search/<name>', views.recipes, name='meal_name'),
]
