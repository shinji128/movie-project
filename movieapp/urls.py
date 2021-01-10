from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('list/', views.List.as_view(template_name='post_list.html'), name="list"),
    path('detail/<pk>/', views.Detail.as_view(template_name='post_detail.html'), name="detail"),
    path('create/', views.Create.as_view(template_name='post_form.html'), name="create")
]
