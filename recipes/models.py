from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

STATUS = ((0, "Draft"), (1, "Published"))

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
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"