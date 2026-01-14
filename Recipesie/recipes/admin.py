from django.contrib import admin
from .models import (
    Recipe, Ingredient, Tag,
    RecipeIngredient, RecipeTag, Review
)
from .admin_site import recipesie_admin_site
from django.contrib.auth.models import User, Group


class IngredientAdmin(admin.ModelAdmin):
    search_fields = ['ingredient']


class TagAdmin(admin.ModelAdmin):
    search_fields = ['tag']


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient')
    list_filter = ('recipe', 'ingredient')


class RecipeTagAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'tag')
    list_filter = ('recipe', 'tag')


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'minutes', 'nsteps', 'contributor')
    list_filter = ('contributor',)
    date_hierarchy = 'date_submitted'
    exclude = ('date_submitted', 'contributor')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('creator', 'rating', 'recipe')
    list_filter = ('recipe', 'rating', 'creator')
    date_hierarchy = 'date_created'


# Register models to CUSTOM admin
recipesie_admin_site.register(Ingredient, IngredientAdmin)
recipesie_admin_site.register(Tag, TagAdmin)
recipesie_admin_site.register(RecipeIngredient, RecipeIngredientAdmin)
recipesie_admin_site.register(RecipeTag, RecipeTagAdmin)
recipesie_admin_site.register(Recipe, RecipeAdmin)
recipesie_admin_site.register(Review, ReviewAdmin)


