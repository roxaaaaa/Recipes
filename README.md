# 🍽️ Django Recipes Application

A web-based recipe management system built with Django that allows users to create, browse, and manage cooking recipes.

## ✨ Features

- **User Authentication**: Register, login, and manage user profiles
- **Recipe Management**: Create, read, update, and delete recipes
- **Ingredient Tracking**: Organize ingredients with measurements
- **Category System**: Categorize recipes (e.g., vegetarian, dessert, main course)
- **Image Uploads**: Add photos to your recipes
- **Search Functionality**: Find recipes by name, ingredient, or category

## 🛠️ Technology Stack

- **Backend**: Django 4.x
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default) / PostgreSQL (production-ready)
- **Static Files**: Django staticfiles handling
- **Templates**: Django template language


## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/roxaaaaa/Recipes.git
   cd Recipes
2. **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
   
3. **Install dependencies**
    ```bash
    pip install django pillow
    
4. **Set up the database**
    ```bash
    python manage.py migrate
    
5. **Create a superuser**
    ```bash
    python manage.py createsuperuser
    
6.**Run the development server**
    ```bash
    python manage.py runserver
    
7.**Visit the application**

  Main site: http://127.0.0.1:8000/
  Admin panel: http://127.0.0.1:8000/admin/

## 📋 Models Overview
  The application includes these main models:
  Recipe: Title, description, instructions, cooking time, difficulty level
  Ingredient: Name, quantity, unit of measurement
  Category: Recipe categories (e.g., Breakfast, Dinner, Dessert)
  UserProfile: Extended user information

## 🔧 Configuration
  Update settings.py for production:
  Set DEBUG = False
  Configure database (PostgreSQL recommended for production)
  Set up static file serving
  Add allowed hosts
  Configure media file storage

## 🤝 Contributing
  Fork the repository
  Create a feature branch (git checkout -b feature/AmazingFeature)
  Commit your changes (git commit -m 'Add some AmazingFeature')
  Push to the branch (git push origin feature/AmazingFeature)
  Open a Pull Request
