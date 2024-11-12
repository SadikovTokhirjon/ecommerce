from django.shortcuts import render ,redirect
from store.models import Product
from django.contrib.auth import authenticate , login,logout

# Create your views here.
def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{'products':products})

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




