from cProfile import Profile
from email.headerregistry import Address
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from .models import Register ,Todo
from django.contrib.auth.models import User
import datetime as dtm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):

    return render(request,'home.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('user_name')
        passwrd = request.POST.get('password')
        print(username,passwrd)
        user = authenticate(request, username=request.POST['user_name'], password=request.POST['password'])
        if user is not None:
            print('Yes auth')
            if user.is_superuser:
                # login(request,user)
                print('supersuer')
                messages.warning(request,'Superuser is not allowed.')
                # return render(request,'error.html')
                return redirect('home')
            elif user.is_staff:
                print('staff')
                messages.warning(request,'Staff are not allowed.')
                # return render(request,'error.html')
                return redirect('home')
            elif user.is_active:
                print('simple user')
                login(request, user)
                messages.success(request,'Successfully login.')
                return render(request,'createtodo.html')
            elif user.is_anonymous:
                print('anonymous')
                messages.warning(request,'You are not having permission to login.')
                return redirect('home')
            else:
                print('Invalid user')
                messages.warning(request,'Invalid user.')
                return redirect('home')
        else:
            print('No auth')
            messages.warning(request,"Your username or password is not correct.")
            return redirect('home')
    
    return render(request,'home.html')


def logout_view(request):
    logout(request)
    messages.success(request,'Successfully logout.')
    return redirect('home')

def register(request):
    if request.method == "POST":
        Name = request.POST.get('name')
        phone_number = request.POST.get('p_num')
        address = request.POST.get('add')
        date_of_birth = request.POST.get('dob')
        email = request.POST.get('eml')
        profile_pics = request.FILES['pic']
        passwrod1 = request.POST.get('pswd')
        password2 = request.POST.get('pswd1')
        print(Name,phone_number,address,date_of_birth,email,profile_pics,passwrod1,password2)
        if passwrod1 == password2:
            user_details = User.objects.create(username= email,email=email,first_name= Name,password=password2)
            register_details = Register(Users=user_details,Phone_number=phone_number,
                Address=address,DOB=date_of_birth,Profile_pic = profile_pics)
            # user_details.save()
            register_details.save()
            messages.success(request,'Successfully got register.')
            return redirect('home')
        else:
            messages.success(request,'Password is does not matched.')
            return render(request,'register.html')


    
    return render(request,'register.html')

@login_required
def create_todo(request):
    if request.method == "POST":
        title = request.POST.get('ttl')
        context = request.POST.get('cnt')
        print(title,context)
        user_details = Register.objects.get(Users=request.user)
        todo = Todo(User_details=user_details,Title=title,Content= context)
        todo.save()
        messages.success(request,'Successfully created todo.')
        return render(request, 'createtodo.html')
    return render(request, 'createtodo.html')

@login_required
def list(request):
    user_details = Register.objects.get(Users=request.user)
    todo = Todo.objects.filter(User_details= user_details)

    return render(request, 'list.html',context={'todo':todo})

@login_required
def completed(request):
    user_details = Register.objects.get(Users=request.user)
    todo = Todo.objects.filter(User_details= user_details,Completed = True)
    return render(request, 'completed_todo.html',context={'todo':todo})

@login_required
def edit(request,pk):
    print(pk)
    if request.method == "GET":
        todo = Todo.objects.get(id = pk)
        return render(request, 'edit.html',context={'todo':todo})

@login_required
def delete(request,pk):
    todo = Todo.objects.get(id = pk)
    todo.delete()
    messages.success(request,'Successfully deleted todo.')
    return redirect('todolist')

@login_required
def edit_todo(request):
    if request.method == "POST":
        id_v = request.POST.get('id_val')

        title = request.POST.get('ttl')
        context = request.POST.get('cnt')
        comp = request.POST.get('cmt')
        print(title,context,comp)
        todo = Todo.objects.get(id = int(id_v))
        todo.Title = title
        todo.Content = context
        if comp == "on":
            todo.Completed = True
            todo.Completion_date = dtm.datetime.now()
        todo.save()
        messages.success(request,'Successfully updated todo.')
        return redirect('todolist')
    