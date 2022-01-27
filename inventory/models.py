from statistics import quantiles
from tkinter import CASCADE
from zoneinfo import available_timezones
from django.db import models
# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField(default=0.00)
    unit = models.CharField(max_length= 100)
    unit_price = models.FloatField(default = 0.00)

    def __str__(self):
        return "Ingredient = {}, Availability = {}, Unit = {}, price per unit = {}".format(self.name, self.quantity, self.unit, self.unit_price)

class MenuItems(models.Model):
    title = models.CharField(max_length= 100)
    price = models.FloatField(default= 0.00)

    def __str__(self):
        return f"Item = {self.title}, Item Price = {self.price}"

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItems, on_delete = models.CASCADE)
    ingredient = models.ForeignKey(Ingredient,  on_delete = models.CASCADE)
    quantity = models.FloatField(default= 0)

    def __str__(self):
        return f"Menu Item = [{self.menu_item.__str__()}], Ingredient Item = {self.ingredient}, Quantity = {self.quantity}"
class Purchases(models.Model):
    menu_item = models.ForeignKey( MenuItems, on_delete =models.CASCADE)
    timestamp = models.DateField(auto_now = True)

    def __str__(self):
        return f"Menu item = [{self.menu_item.__str__()}], Time Stamp = {self.timestamp}"

