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
    path('create', views.create_todo, name='create'),
    path('todolist', views.list, name='todolist'),
    path('Completed_todo', views.completed, name='Completed_todo'),
    path('edit/<int:pk>', views.edit),
    path('edit_todo', views.edit_todo, name='edit_todo'),
    path('delete/<int:pk>', views.delete),

] 
