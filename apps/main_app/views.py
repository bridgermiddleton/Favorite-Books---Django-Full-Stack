from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def mainpage(request):
    return render(request, "main_app/mainpage.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=pw_hash)
        request.session['userid'] = user.id
        return redirect("/success")

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect("/success")
    else:
        return redirect("/")

def success(request):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid'])
        }
        return render(request, "main_app/successfullogin.html", context)
    else:
        return redirect("/")


def logout(request):
   if 'userid' in request.session:
       del request.session['userid']
   return redirect("/")

# Create your views here.
