from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, postMovieblogForm
from users.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
from .models import Movieinfo, Movieblog
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

def index(request):
    return render(request, 'index.html',)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
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

class MovieList(ListView):
    model = Movieinfo

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_movielist = Movieinfo.objects.filter(movietitle__icontains=q_word)
        else:
            object_movielist = Movieinfo.objects.all()
        return object_movielist

class Userbloglist(ListView):
    model = Movieblog

    def get_queryset(self):
        q_word = self.request.GET.get('username')
        if q_word:
            object_list = Movieblog.objects.filter(user__iexact=q_word)
        return object_list

    #if request.method == "GET":
        #print(request.POST)
        #print(request.POST['movieinfo'])
    #    user = get_object_or_404(User, pk=request.GET('movieinfo'))
    #return render(request, 'userdetail.html', {'user':user})

class MovieDetail(DetailView):
    model = Movieinfo

@login_required
def post_movieblog(request):
    if request.method == "POST":
        #print(request.POST)
        #print(request.POST['movieinfo'])
        #import logging
        #logger = logging.getLogger(__name__)
        #logger.info(request.POST)
        #logger.info(request.POST['movieinfo'])
        movie = get_object_or_404(Movieinfo, pk=request.POST['movieinfo'])
        form = postMovieblogForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('index.html')
    else:
        form = postMovieblogForm
    return render(request, 'post_movieblog.html', {'form':form, 'movie':movie})

class Detail(DetailView):
    model = Movieblog

class List(ListView):
    model = Movieblog

class Update(UpdateView):
    model = Movieblog
    fields = ["title", "body"]

class Delete(DeleteView):
    model = Movieblog
    success_url = "/_delete"

def _delete(request):
    return render(request, 'delete.html',)