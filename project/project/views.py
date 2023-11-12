from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User



def signupPage(request):
    messages_error={
        "password_error": "password or confirmpassword not match",
    }
    if request.method=="POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        pass1=request.POST.get("password1")
        pass2=request.POST.get("password2")
        if pass1!=pass2:
            messages.error(request,messages_error["password_error"])
        else:
            myuser=User.objects.create_user(username=uname,email=email,password=pass1)
            myuser.save()
            return redirect("loginPage")


    return render(request,"signup.html")

def loginPage(request):
    messages_error={
        "login_error": "invalid username or password",
    }

    
    if request.method=="POST":
        myname=request.POST.get("username")
        mypassword=request.POST.get("password")
        user=authenticate(username=myname,password=mypassword)
        if user!=None:
            login(request,user)
            messages.success(request,"succsessfuly login")
            return redirect("homePage")
        else:
            messages.error(request,messages_error["login_error"]) 
    
    return render(request,"login.html")


def homePage(request):
    return render(request,"home.html")



def logoutPage(request):
    logout(request)
    return redirect("loginPage")