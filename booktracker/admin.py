from django.contrib import admin
from .models import Book, Author, Progres, Mood, BookReview, BookUsers, ObjectiveReadingBook, ObjectiveYear, BookStatus


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'page_num', 'author', 'translator')
    list_filter = ('id',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Progres)
class ProgresAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'end_time', 'mood',)


@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'book', 'user', 'rating')


@admin.register(BookUsers)
class BookUsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'status')


@admin.register(ObjectiveReadingBook)
class ObjectiveReadingBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'goal_read_book')


@admin.register(ObjectiveYear)
class ObjectiveYearAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'goal_year')



@admin.register(BookStatus)
class BookStatusAdmin(admin.ModelAdmin):
    list_display = ('name', )
