from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
from .models import movieblog
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#import json # 追加
#import requests # 追加
# Create your views here.

def index(request):
    return render(request, 'index.html',)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): #入力された値にエラーが無いかを確認する
            new_user = form.save()
            input_email = form.cleaned_data['email']
            input_password = form.cleaned_data['password1']
            new_user = authenticate(email=input_email, password=input_password)
            if new_user is not None:
                login(request, new_user)
                return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

class List(ListView):
    model = movieblog

class Detail(DetailView):
    model = movieblog

class Create(CreateView):
    model = movieblog
    # 編集対象のフィールド
    fields = ["title", "body", "category", "tags", "movietitle"]
    def form_valid(self, form):
        user = self.request.user
        data = form.cleaned_data
        title = data['title']
        body = data['body']
        category = data['category']
        tags = data['tags']
        movietitle = data['movietitle']
        movie_blog = movieblog.objects.create(user=user,
                                              title=title,
                                              body=body,
                                              category=category,
                                              movietitle=movietitle)
        movie_blog.tags.set(tags)
        return redirect('index')

class Update(UpdateView):
    model = movieblog
    fields = ["title", "body", "category", "tags", "movietitle"]

class Delete(DeleteView):
    model = movieblog
    success_url = "/_delete"

def _delete(request):
    return render(request, 'delete.html',)