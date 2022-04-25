from django.contrib import admin
from django.urls import path
from apps_name import views

urlpatterns = [

          # path('homepage/', views.homepage, name='homepage'),
          # path('', views.Contract, name='Contract'),
          # path('About/', views.About, name='About'),
          path('home/', views.home, name='home'),
          path('About/', views.About, name='About'),
          path('form/', views.form, name='form'),
]
