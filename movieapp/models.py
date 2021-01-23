from django.db import models
from django.urls import reverse_lazy
from users.models import User, UserManager
from moviedb.models import Movieinfo

class movieblog(models.Model):

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