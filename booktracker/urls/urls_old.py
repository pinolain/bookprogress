from django.urls import path
from booktracker import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('booklist', views.book_list),
    path('login/', LoginView.as_view()),
    path('addbook/', views.add_book),
    path('mybooks', views.mybooks),
    path('book/<int:id>', views.book_read),
    path('book/<int:id>/add', views.add_book_to_list)
]
