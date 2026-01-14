from django.contrib.admin import AdminSite

class RecipesieAdminSite(AdminSite):
    site_header = "Recipesie Administration"
    site_title = "Recipesie Admin"
    index_title = "Recipesie Management"


recipesie_admin_site = RecipesieAdminSite(name="recipesie_admin")