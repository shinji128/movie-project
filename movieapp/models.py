from django.db import models
from django.urls import reverse_lazy
from users.models import User, UserManager

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

    movietitle = models.CharField(
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
        return self.movietitle

    def get_absolute_url(self):
        return reverse_lazy("moviedetail", args=[self.id])

class Movieblog(models.Model):

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
    
    user = models.ForeignKey(
        User,
        max_length=200,
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    movieinfo = models.ForeignKey(
        Movieinfo,
        max_length=200,
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    title = models.CharField(
        max_length=200,
        null=False,
        blank=False)
    
    body = models.TextField(
        blank=True,
        null=False)
  
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("detail", args=[self.id])

class FavUser(models.Model):
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='send_user')
    
    user2 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='receive_user')