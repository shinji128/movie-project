from django.db import models
from django.urls import reverse_lazy
import json# 追加
import requests # 追加
#from .forms import MovieForm # 追加

# Create your models here.

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

class Query(models.Model):
    name = models.TextField(
        max_length=300,
        null=True,
        blank=True)

class Query(models.Model):
    name = models.TextField(
        max_length=300,
        null=True,
        blank=True)
    
    def __str__(self): #カテゴリーの自分自信の名前を示す
        return self.name

class Post(models.Model):

    def search_movies(query):
        URL ='https://api.themoviedb.org/3/search/movie?api_key='
        params = {}
        params[api_key]='edd5e5230b0640a802eeb3026214887b'
        params[language]='&language=ja&query='
        params[query]= query
        query = models.TextField(
            max_length=200,
            null=True,
            blank=True)
        params[page]='&page=10'
        params[include_adult]='&include_adult=False'
        response = requests.get(url, params)
        results = response.json() #jsonでレスポンスを表示
        movietitle = results['title']
        return movietitle

    created = models.DateTimeField( #記事作成時に自動で時間を入力
        auto_now=True, #新規作成時にのみ時間が入力され、編集時には追加されない
        editable=False, #ユーザーが編集できないように設定
        null=False,
        blank=False)

    update = models.DateTimeField(
        auto_now=True, #編集した時の時間を追加
        editable=False,
        null=False,
        blank=False)
    
    query = models.TextField(
        blank=True,
        null=True) 

    movietitle = models.CharField(
        max_length=200,
        blank=True,
        null=True)

    title = models.CharField(
        max_length=200,
        null=False,
        blank=False)
    
    body = models.TextField(
        blank=True,
        null=False)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE) #カテゴリーが削除されたらCASCADEで記事も削除されるように設定されている

    tags = models.ManyToManyField(
        Tag, #実際にどのブログのことなのかを指定
        blank=True)
  
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("detail", args=[self.id])
