from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Movietitle)
class MovietitleAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(models.movieblog)
class PostAdmin(admin.ModelAdmin):
    pass