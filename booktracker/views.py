from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import BookUsers, Book
from .forms import BookForm
# Create your views here.
@login_required
def book_list(request):
    book_lst = Book.objects.all()
    return render(request, "booktracker/book_list.html",{'book_list':book_lst})

def add_book(request):
    if request.method == 'GET':
        form = BookForm()
        return render(request, "booktracker/add_book.html", {'form':form})
    book = BookForm(request.POST)
    if book.is_valid():
        book.save()
        return redirect(book_list)

    print(request)
