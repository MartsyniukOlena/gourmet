from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'tags', 'created_on')
    search_fields = ['title', 'tags']
    list_filter = ('status', 'tags', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Comment)