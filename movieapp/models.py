from django.db import models
from django.urls import reverse_lazy

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
        max_length=255,
        null=False,
        blank=False)
    
    def __str__(self): #カテゴリーの自分自信の名前を示す
        return self.name


class Post(models.Model):
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

    def get_absoluto_url(self):
        return reverse_lazy("movieapp:detail", [self.pk])