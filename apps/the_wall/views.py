from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message, Comment

def wallpage(request):
    if 'userid' in request.session:
        context = {
            "all_the_messages": Message.objects.all(),
            "user": User.objects.get(id=request.session['userid'])
        }
        return render(request, "the_wall/wallpage.html", context)
    else:
        return redirect("/")

def postmessage(request):
    Message.objects.create(user=User.objects.get(id=request.session['userid']),message=request.POST['message'])
    return redirect("/wall")

def postcomment(request, messageid):
    Comment.objects.create(user=User.objects.get(id=request.session['userid']),message=Message.objects.get(id=messageid), comment=request.POST['comment'])
    return redirect("/wall")

def deletecomment(request, commentid):
    Comment.objects.get(id=commentid).delete()
    return redirect("/wall")

def deletemessage(request, messageid):
    Message.objects.get(id=messageid).delete()
    return redirect("/wall")

    

# Create your views here.
