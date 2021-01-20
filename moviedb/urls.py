from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('movielist/', views.List.as_view(template_name='movielist.html'), name="movielist"),
    path('moviedetail/<pk>/', views.Detail.as_view(template_name='moviedetail.html'), name="moviedetail"),
]
#post_list.html