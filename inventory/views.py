from dataclasses import fields
from re import template
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import MenuItems, Ingredient, RecipeRequirement, Purchases
from .forms import CreatePurchaseForm, UpdateIngredientItemForm, UpdateMenuItemForm, UpdateRecipeRequirementForm



# Create your views here.



def home(request):
    queryset = Ingredient.objects.all()
    queryset1 = Purchases.objects.all()
    queryset2 = MenuItems.objects.all()
    context = {
        'ingredient_list': queryset,
        'purchases_list' : queryset1,
        'menu_list' : queryset2
    }
    return render(request, "inventory/home.html", context)




class MenuItemList(ListView):
    model = MenuItems
    template_name = "menu_list.html"

class IngredientList(ListView):
    model = Ingredient
    template_name = "ingredient_list.html"

# class RecipeRequirementList(ListView):
#     model = RecipeRequirement
#     template_name = ""

class PurchasesList(ListView):
    model = Purchases
    template_name = "purchases_list_html"

class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = ""
    fields = ["name", "quantity","unit","unit_price"]

# class PurchasesDelete(DeleteView):
#     model = Purchases
#     template_name = ""
#     fields = ["menu_item", "timestamp"]


class CreateViewPurchase(CreateView):
    model = Purchases
    template_name = "add_purchase.html"
    form_class = CreatePurchaseForm
