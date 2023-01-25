from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Author, BookUsers, Book, Progres
from .forms import BookForm, ProgresForm, ProgresFormBook, AuthorForm
from django.views.generic.list import ListView
# Create your views here.
@login_required
def book_list(request):
    book_lst = Book.objects.all()
    return render(request, "booktracker/book_list.html", {'book_list': book_lst})


class BookList(ListView):
    model = Book
    template_name = 'booktracker/book_list.html'




def add_book(request):
    if request.method == 'GET':
        form = BookForm()
        return render(request, "booktracker/add_book.html", {'form': form})
    book = BookForm(request.POST)
    if book.is_valid():
        author = book.data.get('author')
        new_author = book.data.get('new_author')
        if (author and new_author) or (not(author or new_author)):
            return render(request, 'booktracker/404.html', status=404)

        if author:
            book.save()
        if new_author:
            new_author_obj = Author.objects.create(name=book.data.get('new_author'))
            new_book = book.save(commit=False)
            new_book.author = new_author_obj
            new_book.save()
        return redirect(book_list)
    else:
        print(book.errors)
        return render(request, "booktracker/add_book.html", {'form': book})


def mybooks(request):
    mybooks = BookUsers.objects.filter(user_id=request.user.id)
    return render(request, "booktracker/user_book_list.html", {'mybooks': mybooks})


def book_read(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return render(request, 'booktracker/404.html', status=404)
    if request.method == 'GET':
        last_progres = Progres.objects.filter(book=book, user_id=request.user.id).order_by('-end_time').first()
        if last_progres:
            start_page = last_progres.end_page
        else:
            start_page = 0
        form = ProgresFormBook(initial={'start_page': start_page})

        return render(request, 'booktracker/book.html', {'form': form, 'book': book})
    progres = ProgresFormBook(request.POST)
    if progres.is_valid():
        instance = progres.save(commit=False)
        instance.user = request.user
        instance.book = book
        instance.save()
        return redirect(book_read, id)


def add_book_to_list(request, id):
    book_user = BookUsers.objects.create(user=request.user, book_id=id)
    return redirect(mybooks)



