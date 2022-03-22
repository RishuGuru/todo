from django.contrib import admin
from django.urls import path,include
from .views import home,login
# from 
urlpatterns = [
    path('', home, name='home'),
    path('login', login, name='login'),
] 
