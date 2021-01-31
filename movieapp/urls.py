from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('movielist/', views.MovieList.as_view(template_name='movielist.html'), name='movielist'),
    path('moviedetail/<pk>/', views.MovieDetail.as_view(template_name='moviedetail.html'), name="moviedetail"),
    path('post_movieblog/', views.post_movieblog, name='post_movieblog'),
    path('list/', views.List.as_view(template_name='list.html'), name='list'),
    path('detail/<pk>/', views.Detail.as_view(template_name='post_detail.html'), name="detail"),
    #path('userlist/', views.Detail.as_view(template_name='userlist.html'), name="userlist"),
    path('userbloglist/<pk>/', views.Userbloglist.as_view(template_name='userbloglist.html'), name='userbloglist'),
    #path('create/<pk>', views.Create.as_view(template_name='post_form.html'), name="create"),
    path('update/<pk>/', views.Update.as_view(template_name='post_form.html'), name="update"),
    path('delete/<pk>', views.Delete.as_view(template_name='post_confirm_delete.html'), name="delete"),
    path('_delete/', views._delete, name='_delete'),
    path('fav_users/', views.fav_users, name='fav_users'),
    path('toggle_fav_receive_user_status/', views.toggle_fav_receive_user_status, name='toggle_fav_receive_user_status'),
]
#post_list.html
#path('list/', views.Movielist.as_view(template_name='movielist.html'), name='movielist'),
#path('detail/<pk>/', views.Moviedetail.as_view(template_name='moviedetail.html'), name="moviedetail"),