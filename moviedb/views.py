from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import movieblog
from django.views.generic.edit import CreateView, UpdateView
#import json # 追加
#import requests # 追加
# Create your views here.

def index(request):
    return render(request, 'index.html',)

class List(ListView):
    model = Movieinfo

class Detail(DetailView):
    model = Movieinfo

class Mcreate(CreateView):
    model = Movieinfo
    # 編集対象のフィールド
    fields = ["title", "director", "release",]