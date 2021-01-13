from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
from .models import Post
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
    model = Post
    #paginate_by = 10 #10個だけ表示
    queryset = model.objects.order_by('-created')
    #def get_queryset(self): #フィルタ表示
    #return Post.objects.filter(
class Detail(DetailView):
    model = Post

class Create(CreateView):
    model = Post
    # 編集対象のフィールド
    fields = ["title", "body", "category", "tags", "movietitle", "query"]

class Update(UpdateView):
    model = Post
    fields = ["title", "body", "category", "tags", "movietitle", "query"]

class Delete(DeleteView):
    model = Post
    success_url = "/_delete"

def _delete(request):
    return render(request, 'delete.html',)

#def search_movies(search_word):
#    URL ='https://api.themoviedb.org/3/search/movie?api_key=
#    params = {}
#    params[api_key]='edd5e5230b0640a802eeb3026214887b'
#    params[language]='&language=ja&query='
#    params[query]=TextField()
#    params[page]='&page=10'
#    params[include_adult]='&include_adult=False'
#    response = requests.get(url, params)
#    results = response.json() #jsonでレスポンスを表示
#    results['title']
#    return title