from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):
    if(request.method=="POST"):
        fst_name=request.POST['fst_name']
        lst_name=request.POST['lst_name']
        email=request.POST['email']
        user=request.POST['user']
        pass1=request.POST['pass']
        pass2=request.POST['c_pass']
        if(pass1!=pass2):
            messages.info(request,'password not match')
            return render(request,'register.html')
        elif User.objects.filter(username=user).exists():
            messages.info(request,'user taken')
            return render(request,'register.html')
        elif User.objects.filter(email=email).exists():
             messages.info(request,'Email exists')
             return render(request,'register.html') 

        else:
            userr=User.objects.create_user(first_name=fst_name,last_name=lst_name,email=email, username=user, password=pass1)
            userr.save();
            messages.info(request,'account created')
            return redirect('login')
    else:
        return render(request,'register.html')
    return render(request,'register.html')
def login(request):
    if request.method=="POST":
        user=request.POST['user']
        password=request.POST['password']
        userr=auth.authenticate(username=user,password=password)
        if userr is not None:
            auth.login(request,userr)
            return redirect('/')
        else:
            messages.info(request,'Invalid user or password')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')