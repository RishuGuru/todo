from cProfile import Profile
from email.headerregistry import Address
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from .models import Register
from django.contrib.auth.models import User
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
                return render(request,'todo.html')
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
    # {% comment %} Users = models.OneToOneField(User, on_delete=models.CASCADE)
    # Phone_number = models.CharField(max_length=10)
    # Address = models.CharField(max_length=100)
    # DOB = models.DateField(auto_created=False,auto_now=False)
    # DOJ = models.DateTimeField(auto_created=False,auto_now=False,default=dtm.now)
    # Profile_pic = models.ImageField('media') {% endcomment %}
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