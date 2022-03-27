from django.contrib import admin
from django.urls import path,include
from .views import home,login_view,logout_view
from . import views
# from 
urlpatterns = [
    path('', home, name='home'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('register', views.register, name='register'),
    # path('logout', logout_view, name='logout'),
] 
