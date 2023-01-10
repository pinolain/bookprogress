from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('book_list', views.book_list),
    path('login/', LoginView.as_view()),
    path('add_book/', views.add_book)
]
