from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, default='')
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="recipe_posts")
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.PositiveIntegerField(help_text='Time in minutes', default=0)
    EASY = 'Easy'
    MODERATE = 'Moderate'
    DIFFICULT = 'Difficult'
    DIFFICULTY_CHOICES = [
        (EASY, 'Easy'),
        (MODERATE, 'Moderate'),
        (DIFFICULT, 'Difficult'),
    ]
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()