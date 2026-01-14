"""
URL configuration for Recipesie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from recipes import views
import recipes.bienvenu
from recipes.admin_site import recipesie_admin_site

urlpatterns = [
    # Create , edit recipes paths
    path('Recipesie/recipes/add/', views.add_edit_recipe, name='add_recipe'),
    path('Recipesie/recipes/edit/<int:pk>/', views.add_edit_recipe, name='edit_recipe'),

    # Images
    path('Recipesie/recipes/update_image/<int:pk>/', views.update_recipe_image, name='update_recipe_image'),

    path('Recipesie/search/', views.search_recipes, name='search'),
    path('Recipesie/home/', recipes.bienvenu.Bienvenu.as_view(), name='home'),
    path('Recipesie/recipes/', views.recipes_list, name='recipes_list'),
    path('Recipesie/recipes/detail/', views.recipe_detail, name='recipe_detail'),
    path('Recipesie/recipes_reviews/detail/', views.details_reviews, name='details_reviews'),

    path('admin/', admin.site.urls),
    path('Recipesie/admin/', recipesie_admin_site.urls),
]

# Static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)