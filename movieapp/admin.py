from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Movieblog)
class MovieblogAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Movieinfo)
class MovieinfoAdmin(admin.ModelAdmin):
    pass