from ast import In
from dataclasses import fields
from re import purge
from django import forms
from .models import Ingredient, Purchases, MenuItems, RecipeRequirement

class CreateMenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItems
        fields = "__all__"

class CreateIngredientItemForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class UpdateRecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"

class CreatePurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchases
        fields = "__all__"


class UpdateIngredientForm(forms.ModelForm):
    class Meta:
        model =Ingredient
        fields = "__all__"



