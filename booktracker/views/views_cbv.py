from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from booktracker.models import Author, BookUsers, Book, Progres
from booktracker.forms import BookForm, ProgresForm, ProgresFormBook, AuthorForm
from django.views.generic import View, TemplateView, FormView, ListView, DetailView, CreateView


class BookList(View):
    def get(self, request, *args, **kwargs):
        book_lst = Book.objects.all()
        return render(self.request, "booktracker/book_list.html", {'book_list': book_lst})


class AddBook(View):
    def get(self, request, *args, **kwargs):
        form = BookForm()
        return render(request, "booktracker/add_book.html", {'form': form})

    def post(self, request, *args, **kwargs):
        def add_book(request):
            if request.method == 'GET':
                form = BookForm()
                return render(request, "booktracker/add_book.html", {'form': form})
            book = BookForm(request.POST)
            if book.is_valid():
                author = book.data.get('author')
                new_author = book.data.get('new_author')
                if (author and new_author) or (not (author or new_author)):
                    return render(request, 'booktracker/404.html', status=404)

                if author:
                    book.save()
                if new_author:
                    new_author_obj = Author.objects.create(name=book.data.get('new_author'))
                    new_book = book.save(commit=False)
                    new_book.author = new_author_obj
                    new_book.save()
                return redirect('cbv/booklist')
            else:
                print(book.errors)
                return render(request, "booktracker/add_book.html", {'form': book})


class UserBookList(TemplateView):
    template_name = 'booktracker/user_book_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mybooks'] = BookUsers.objects.filter(user_id=self.request.user.id)
        return context


class CreateBookProgress(FormView):

    form_class = ProgresFormBook
    template_name = 'booktracker/book.html'

    def get_initial(self):
        try:
            book = Book.objects.get(id=self.kwargs.get('id'))
        except Book.DoesNotExist:
            return render(self.request, 'booktracker/404.html', status=404)
        last_progres = Progres.objects.filter(book=book, user_id=self.request.user.id).order_by('-end_time').first()
        if last_progres:
            start_page = last_progres.end_page
        else:
            start_page = 0
        return {'start_page': start_page}

    def get_success_url(self):
        """
        
        :return:
        """
        return f'/cbv/book/{self.kwargs.get("id")}'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.book_id = self.kwargs.get('id')
        instance.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.get(id= self.kwargs.get('id'))
        return context

