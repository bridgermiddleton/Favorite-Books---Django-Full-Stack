from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book


def booksmainpage(request):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            "all_the_books": Book.objects.all(),
        }
        return render(request, "favorite_books/booksmainpage.html", context)

def addbook(request):
    errors = Book.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/books")
    else:
        newBook = Book.objects.create(title=request.POST['title'],description=request.POST['description'],uploaded_by=User.objects.get(id=request.session['userid']))
        user = User.objects.get(id=request.session['userid'])
        newBook.users_who_like.add(user)
        return redirect("/books")

def bookdetails(request, bookid):
    thebook = Book.objects.get(id=bookid)
    context = {
        "user": User.objects.get(id=request.session['userid']),
        "book": Book.objects.get(id=bookid),
        "users_who_like": thebook.users_who_like.all()
    }
    return render(request, "favorite_books/bookdetails.html", context)

def update(request, bookid):
    c = Book.objects.get(id=bookid)
    c.description = request.POST['description']
    c.save()
    return redirect(f"/books/{bookid}")

def deletebook(request, bookid):
    Book.objects.get(id=bookid).delete()
    return redirect("/books")

def favorite(request, bookid):
    this_user = User.objects.get(id=request.session['userid'])
    this_book = Book.objects.get(id=bookid)
    this_user.liked_books.add(this_book)
    return redirect(f"/books/{bookid}") 
def unfavorite(request, bookid):
    this_user = User.objects.get(id=request.session['userid'])
    this_book = Book.objects.get(id=bookid)
    this_user.liked_books.remove(this_book)
    return redirect(f"/books/{bookid}")

# Create your views here.
