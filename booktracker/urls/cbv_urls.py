from django.urls import path
from booktracker import views
from django.contrib.auth.views import LoginView, LogoutView
from booktracker.views.views_cbv import BookList, UserBookList, AddBook, CreateBookProgress


urlpatterns = [
    path('booklist', BookList.as_view()),
    path('login/', LoginView.as_view()),
    path('addbook/', AddBook.as_view()),
    path('mybooks', UserBookList.as_view()),
    path('book/<int:id>', CreateBookProgress.as_view()),
    path('book/<int:id>/add', views.add_book_to_list)
]
