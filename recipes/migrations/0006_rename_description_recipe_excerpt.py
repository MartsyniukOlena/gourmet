# Generated by Django 4.2.11 on 2024-03-11 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_recipe_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='description',
            new_name='excerpt',
        ),
    ]