from django.shortcuts import render,redirect,HttpResponse



def signupPage(request):
    return render(request,"signup.html")

def loginPage(request):
    return render(request,"login.html")


def homePage(request):
    return render(request,"home.html")