"""djangodelight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inventory import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("", views.home, name = "home"),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_view,name = "logout" ),
    path("ingredient/list", views.IngredientList.as_view(), name = "ingredientlist"),
    path("ingredient/delete/<pk>", views.IngredientDelete.as_view(), name = "ingredientdelete"),
    path("purchase/list", views.PurchasesList.as_view(), name = "purchaseslist"),
    path("menuitem/list", views.MenuItemList.as_view(), name = "menuitemlist"),
    path("purchase/create", views.CreateViewPurchase.as_view(), name = "createpurchase"),
    path("ingredient/create", views.CreateViewIngredient.as_view(), name = "createingredient"),
    path("menuitem/create", views.CreateViewMenu.as_view(), name = "createmenuitem"),
    path("ingredient/<pk>/update", views.UpdateViewIngredient.as_view(), name = "updateingredient")
    
]
