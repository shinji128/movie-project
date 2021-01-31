from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, postMovieblogForm
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
from .models import Movieinfo, Movieblog, FavUser
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.views.decorators.http import require_POST
# Create your views here.

User = settings.AUTH_USER_MODEL

def index(request):
    return render(request, 'index.html',)

@login_required
def fav_users(request):
    receive_user = FavUser.objects.filter(user=request.user)
    return render(request, 'index.html', {'receive_user': receive_user})

@login_required
@require_POST
def toggle_fav_receive_user_status(request):
    receive_user = get_object_or_404(FavUser, pk=request.POST["user_id"])
    send_user = request.user
    print(request.POST)
    
    # 既にfavが存在するか
    exist_fav_user = FavUser.objects.filter(user=send_user)
    if exist_fav_user.exists():
        FavUser.objects.create(user=send_user,user2=receive_user)
    else:
        exist_fav_user.delete()
    return redirect('userbloglist.html', user_id=send_user.id)


#@login_required
#def fav_users(request):
#    send_user = request.user
#    receive_user = user.fav_users.all()
#    return render(request, 'index.html', {'receive_user': receive_user})

#@login_required
#@require_POST
#def toggle_fav_receive_user_status(request):
#    receive_user = get_object_or_404(FavUser, pk=request.POST["user_id"])
#    send_user = request.user
#    if receive_user in user.fav_users.all():
#        user.fav_users.remove(receive_user)
#    else:
#        user.fav_users.add(receive_user)
#    return redirect('index.html', user_id=user.id)

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
            object_list = Movieinfo.objects.filter(movietitle__icontains=q_word)
        else:
            object_list = Movieinfo.objects.all()
        return object_list

class Userbloglist(ListView):
    model = Movieblog

    def get_queryset(self):
        user = self.request.GET.get('user')
        object_list = Movieblog.objects.filter(user=user)
        return object_list

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