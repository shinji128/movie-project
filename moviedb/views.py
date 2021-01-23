from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Movieinfo
from movieapp.models import movieblog
# Create your views here.

def index(request):
    return render(request, 'index.html',)

class Movielist(ListView):
    model = Movieinfo

class Moviedetail(DetailView):
    model = Movieinfo
    #def get(request, pk):
    #    movie_blog = movieblog.objects.create(Movietitle=Movieinfo.title)
    #    return redirect('http://127.0.0.1:8000/create/pk')

class Moviecreate(CreateView):
    model = Movieinfo
    # 編集対象のフィールド
    fields = ["title", "director", "release",]