from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.movieblog)
class PostAdmin(admin.ModelAdmin):
    pass