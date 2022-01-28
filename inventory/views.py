from dataclasses import fields
from re import template
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import MenuItems, Ingredient, RecipeRequirement, Purchases
from .forms import CreatePurchaseForm, CreateIngredientItemForm, CreateMenuItemForm, UpdateIngredientForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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




class MenuItemList(LoginRequiredMixin,ListView):
    model = MenuItems
    template_name = "menu_list.html"

class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "ingredient_list.html"

    # def post(self, request, *args, **kwargs):
    #     return UpdateIngredientForm(request) # W


# class RecipeRequirementList(ListView):
#     model = RecipeRequirement
#     template_name = ""

class PurchasesList(LoginRequiredMixin, ListView):
    model = Purchases
    template_name = "purchases_list_html"

class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = ""
    fields = ["name", "quantity","unit","unit_price"]

# class PurchasesDelete(DeleteView):
#     model = Purchases
#     template_name = ""
#     fields = ["menu_item", "timestamp"]


class CreateViewPurchase(LoginRequiredMixin, CreateView):
    model = Purchases
    template_name = "inventory/add_purchase.html"
    form_class = CreatePurchaseForm


class CreateViewIngredient(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = "inventory/add_ingredient.html"
    form_class = CreateIngredientItemForm


class CreateViewMenu(LoginRequiredMixin, CreateView):
    model = MenuItems
    template_name = "inventory/add_menu_item.html"
    form_class = CreateMenuItemForm


class UpdateViewIngredient(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = "inventory/update_ingredient.html"
    form_class = UpdateIngredientForm
    success_url = reverse_lazy('ingredientlist')


    # def get_success_url(self) -> str:
    #     return reverse_lazy('ingredientlist')



def logout_view(request):
    logout(request)
    return redirect("home")