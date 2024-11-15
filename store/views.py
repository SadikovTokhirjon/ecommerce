from django.shortcuts import render ,redirect
from store.models import Product
from django.contrib.auth import authenticate , login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.
def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{'products':products})
def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})
def about(request):
    return render(request , 'aboute.html',{})


def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else: return redirect('home')
    else:return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data
            password= form.cleaned_data
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'You are now registered')
            return redirect('home')
        else:
            messages.error(request,'Please correct the error below.')
            return redirect('register')
    else:
        messages.error(request,'Please correct the error below.')
        return render(request,'register.html',{'form':form})


