from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages, auth

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid details")
            return redirect('login')

    else:
        return render(request,'login.html')


def register_view(request):
    if request.method == 'POST':
        userid=request.POST['username']
        email=request.POST['email']
        first_name=request.POST['first_name']
        password=request.POST['password']
        re_password=request.POST['re-password']

        if password==re_password:

            if User.objects.filter(username=userid).exists():
                messages.info(request,'username already taken')
                return redirect(register_view)
            
            else:
                user = User.objects.create_user(username=userid, email=email, password=password,first_name=first_name)
                user.save()
                return redirect('/')
        
        else:

            messages.info(request, 'password not matching')
            return redirect(register_view)
    else:

        return render(request,'sign_up.html')

def logout(request):
    auth.logout(request)
    return redirect('/')