from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import register

app_name = 'mania'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.courts_view, name='courts'),
    path('bookingform/', views.bookingform_view, name='Bookingform'),
    path('home/register', views.register, name='register'),
    path('home/', views.home, name='home'),
    #path('login/', views.login_user, name='login_user'),
    #path('logout/', views.logout_user, name='logout_user'),
    #path("home/register", views.register, name="register"),
    path("login", views.login_user, name="login_user"),
    path("register", views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('/redirect/', register), 
    path("home/login_user", views.login_user, name="login_user"),
    path("home/logout_user", views.logout_user, name="logout_user"),
    #path("home", views.home, name="home")




]