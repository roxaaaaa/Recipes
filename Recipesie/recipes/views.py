from .models  import Recipe, Ingredient,Tag, RecipeTag, RecipeIngredient, Review
from statistics import median
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Recipe
from .forms import RecipeForm, RecipeImageForm
from django.contrib.auth.decorators import login_required

@login_required  # This ensures only logged-in users can add recipes
def add_edit_recipe(request, pk=None):
    recipe = get_object_or_404(Recipe, pk=pk) if pk else None

    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            # Create the object but don't save to DB yet
            new_recipe = form.save(commit=False)

            # Assign the logged-in user as the contributor
            # This fixes the NOT NULL constraint error
            if not pk:
                # Only set contributor if creating a new recipe
                new_recipe.contributor = request.user

            # save the recipe and the ManyToMany data
            new_recipe.save()
            form.save_m2m()

            msg = "Recipe updated successfully!" if pk else "Recipe created successfully!"
            messages.success(request, msg)
            return redirect('search')
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipe_form.html', {'form': form, 'recipe': recipe})

def update_recipe_image(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        # Use RecipeImageForm and include request.FILES
        form = RecipeImageForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image updated successfully!')
            return redirect('search')
    else:
        # FIX: Change RecipeForm to RecipeImageForm here
        form = RecipeImageForm(instance=recipe)

    return render(request, 'update_image.html', {'form': form, 'recipe': recipe})


def search_recipes(request):
    results = []
    # Get the search query and the selected category from the GET request
    query = request.GET.get('q', '').strip()
    category = request.GET.get('category', 'name')
    # 'name' is the default

    if 'q' in request.GET:
        #  Handling empty values
        if not query:
            messages.error(request, "Search cannot be empty. Please enter at least 1 character.")
        else:
            # Initialize an empty queryset
            recipes_qs = Recipe.objects.none()

            # Text: starts with, case-insensitive
            if category == 'name':
                recipes_qs = Recipe.objects.filter(name__istartswith=query)
            elif category == 'ingredient':
                recipes_qs = Recipe.objects.filter(ingredients__ingredient__istartswith=query)
            elif category == 'tag':
                recipes_qs = Recipe.objects.filter(tags__tag__istartswith=query)
            elif category == 'contributor':
                recipes_qs = Recipe.objects.filter(contributor__username__istartswith=query)

            # NUmbers: Less than or equal to
            elif category in ['steps', 'minutes', 'num_ingredients']:
                # Check if input is a valid number
                if query.isdigit():
                    num = int(query)
                    if category == 'steps':
                        recipes_qs = Recipe.objects.filter(nsteps__lte=num)
                    elif category == 'minutes':
                        recipes_qs = Recipe.objects.filter(minutes__lte=num)
                    elif category == 'num_ingredients':
                        recipes_qs = Recipe.objects.filter(ningredients__lte=num)
                else:
                    # Show error if non-numeric value introduced
                    messages.error(request, f"You must introduce a number to search by {category}.")

            # Ensure results are unique
            results = recipes_qs.distinct()

    context = {
        'results': results,
        'query': query,
        'category': category
    }
    return render(request, 'search.html', context)

#Calculates median for the available ratings of the recipe
def median_rating (reviews_ratings):
    return median(reviews_ratings)

def recipes_list(request):
    recipes = Recipe.objects.all()
    recipe_list = list()
    for recipe in recipes:
        reviews = recipe.review_set.all()
        tags=recipe.tags.all()
        ingredients = recipe.ingredients.all()
        if reviews:
            review_ratings = list()
            for review in reviews:
                review_ratings.append(review.rating)
            recipe_rating = str(round(median_rating(review_ratings), 2))
            number_of_reviews = str(len(reviews))
        else:
            recipe_rating = None
            number_of_reviews="0"

        # if tags:
        #     tag_list = list()
        #     for company in production_companies:
        #         production_companies_list.append(company.production_company)
        #
        # if genres:
        #     genres_list = list()
        #     for genre in genres:
        #         genres_list.append(genre.genre)

        recipe_list.append({'recipe': recipe,\
                           'tags': tags, \
                           'ingredients': ingredients, \
                           'recipe_rating': recipe_rating,\
                          'number_of_reviews':number_of_reviews})

    context={
            'recipe_list': recipe_list
        }

    return render(request, 'recipes_list.html', context)

def recipe_detail(request):
    recipe_id = request.GET.get("recipe_id")
    recipe = Recipe.objects.get(id=recipe_id)

    reviews = recipe.review_set.all()

    context = {
        'recipe': recipe,
        'reviews': reviews
    }
    return render(request, 'recipe_detail.html', context)

def details_reviews(request):
    recipe_id = request.GET.get("recipe_id")
    print(recipe_id)
    recipe=Recipe.objects.get(id=recipe_id)
    print(recipe.name)
    reviews = recipe.review_set.all()
    print(reviews)

    context={
        'recipe':recipe,\
        'reviews': reviews,
    }

    return render(request,'recipes_reviews.html', context)


