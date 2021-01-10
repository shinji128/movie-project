from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView

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

class Detail(DetailView):
    model = Post

class Create(CreateView):
    model = Post
    # 編集対象のフィールド
    fields = ["title", "body", "category", "tags"]