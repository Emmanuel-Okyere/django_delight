from ast import In
from dataclasses import fields
from re import purge
from django import forms
from .models import Ingredient, Purchases, MenuItems, RecipeRequirement

class UpdateMenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItems
        fields = "__all__"

class UpdateIngredientItemForm(forms.ModelForm):
    class Meta:
        models = Ingredient
        fields = "__all__"

class UpdateRecipeRequirementForm(forms.ModelForm):
    class Meta:
        models = RecipeRequirement
        fields = "__all__"

class CreatePurchaseForm(forms.ModelForm):
    class Meta:
        models = Purchases
        fields = "__all__"
