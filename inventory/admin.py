from django.contrib import admin
from .models import Purchases, MenuItems, Ingredient, RecipeRequirement
# Register your models here.
admin.site.register(Purchases)
admin.site.register(Ingredient)
admin.site.register(MenuItems)
admin.site.register(RecipeRequirement)