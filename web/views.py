# from django.shortcuts import render
# from .models import PlacedModel

# # Create your views here.

# def home(request):
#     data=PlacedModel.objects.all()
#     return render(request,'home.html',context={'data':data})


from django.shortcuts import render,redirect,HttpResponse
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

# Create your views here.
def register(request):
    if request.method=='POST':
        u=User.objects.filter(username=request.POST['username'])
        if u.exists():
            messages.info(request,'username already exist')
            return redirect('/register/')
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    f=RegisterForm()
    return render(request,'register.html',context={'form':f})

def login_view(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user:
                login(request,user)
                # return HttpResponse("<h1>Login SuccessFull</h1>")
                return redirect(reverse('web:home'))
                #return render(request,'home.html')
            else:
                messages.info(request,'Username or password is not valid')
                return redirect('/login/')
    f=LoginForm()
    return render(request,'login.html',context={'form':f})


def home(request):
    return render(request,'home.html')

def trainers(request):
    return render(request,'trainers.html')

def courses(request):
    return render(request,'courses.html')

def contact(request):
    return render(request,'contact.html')

def enquiry(request):
    return render(request,'enquiry.html')

def detail(request):
    return render(request,'detail.html')

def about(request):
    return render(request,'about.html')

def logout_view(request):
    logout(request,User)
    #return redirect(reverse('web:login'))
    return render(request,'register.html')