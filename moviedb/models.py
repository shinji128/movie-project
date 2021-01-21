from django.db import models
from django.urls import reverse_lazy

class Category(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True)
    
    def __str__(self): #カテゴリーの自分自信の名前を示す
        return self.name

class Tag(models.Model):
    name = models.CharField(
        max_length=300,
        null=False,
        blank=False)

    def __str__(self): #カテゴリーの自分自信の名前を示す
        return self.name

class Movieinfo(models.Model):

    title = models.CharField(
        max_length=200,
        blank=True,
        null=True)

    director = models.CharField(
        max_length=200,
        null=False,
        blank=False)

    release = models.DateField(
        auto_now=False,
        auto_now_add=False, 
        null=False,
        blank=False)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE)

    tags = models.ManyToManyField(
        Tag,
        blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("moviedetail", args=[self.id])