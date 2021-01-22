from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Movieinfo
# Create your views here.

def index(request):
    return render(request, 'index.html',)

class Movielist(ListView):
    model = Movieinfo

class Moviedetail(DetailView):
    model = Movieinfo

class Moviecreate(CreateView):
    model = Movieinfo
    # 編集対象のフィールド
    fields = ["title", "director", "release",]