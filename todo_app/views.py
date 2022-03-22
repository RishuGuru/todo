from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.

def home(request):

    return render(request,'home.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('user_name')
        passwrd = request.POST.get('password')
        print(username,passwrd)
        user = authenticate(username=username, password=passwrd)
        if user is not None:
            print('Yes auth')
            if user.is_superuser:
                # login(request,user)
                print('supersuer')
                messages.warning(request,'Superuser is not allowed')
                # return render(request,'error.html')
                return redirect('home')
            elif user.is_staff:
                print('staff')
                messages.warning(request,'Staff are not allowed')
                # return render(request,'error.html')
                return redirect('home')
            elif user.is_active:
                print('simple user')
            elif user.is_anonymous:
                print('anonymous')
            else:
                print('Invalid user')
            pass
        else:
            print('No auth')

            # No backend authenticated the credentials
            pass
    
    return render(request,'todo.html')