from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['recipe_img', 'date_submitted', 'contributor']
        fields = '__all__'
        # Adding placeholders and setting number field steps
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter recipe name'}),
            'minutes': forms.NumberInput(attrs={'placeholder': 'Prep time', 'step': '1'}),
            'n_steps': forms.NumberInput(attrs={'placeholder': 'Steps count', 'step': '1'}),
            'n_ingredients': forms.NumberInput(attrs={'placeholder': 'Ingredients count', 'step': '1'}),
            'description': forms.Textarea(attrs={'placeholder': 'High level description of the recipe'}),
            'steps': forms.Textarea(attrs={'placeholder': 'Detailed steps involved in preparation'}),
        }

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_img']