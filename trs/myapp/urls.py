from django.contrib import admin
from django.urls import path
from django.urls import include
from myapp import views

urlpatterns = [
    path('', views.home),
    path('register',views.register),
    path('login',views.login),
    path('about',views.about),
    path('leaderboard',views.leaderboard),
    path('rate',views.rate),
    path('logout',views.logout),
]