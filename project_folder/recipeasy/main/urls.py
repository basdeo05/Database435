from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('results/', views.categories, name='search'),
    path('results/<meal_name>', views.recipes, name='meal_name'),
]
