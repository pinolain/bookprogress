from django.db import models
from django.conf import settings
from django.utils import timezone


class Author(models.Model):
    name = models.CharField('Имя автора', max_length=155, unique=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Mood(models.Model):
    name = models.CharField('Название эмоции', max_length=20)

    class Meta:
        verbose_name = 'Настроение после чтения'
        verbose_name_plural = 'Настроения после чтений'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField('Название книги', max_length=155)
    page_num = models.IntegerField('Количество страниц')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Автор книги')
    translator = models.CharField('Переводчики', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        unique_together = ('title', 'page_num', 'author')

    def __str__(self):
        return self.title


class Progres(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    start_time = models.DateTimeField('Начало чтения', default=timezone.now)
    end_time = models.DateTimeField('Окончание чтения', default=timezone.now)
    start_page = models.IntegerField('Начальная страница')
    end_page = models.IntegerField('Страница окончания')
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE, null=True, verbose_name='Настроение')

    class Meta:
        verbose_name = 'Чтение'
        verbose_name_plural = 'Чтения'

    def __str__(self):
        return f'{self.book.title}-{self.user.username}-{str(self.end_time)}'  # str(self.book)


class BookStatus(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Статус книги'
        verbose_name_plural = 'Статусы книг'

    def __str__(self):
        return self.name


class BookUsers(models.Model):  # "Связь книга - пользователь"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, verbose_name='Книга')
    completed_date = models.DateField('Дочитана', null=True, blank=True)
    planed_complete = models.DateField('Нужно дочитать', null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    status = models.ForeignKey(BookStatus, on_delete=models.RESTRICT, null=False, blank=False)

    class Meta:
        verbose_name = 'Книг пользователя'
        verbose_name_plural = 'Книги пользователя'
        unique_together = ('user', 'book')

    def __str__(self):
        return f'{self.book} {self.user.name}'


class Attachment(models.Model):
    text = models.TextField()
    bookusers = models.ForeignKey(BookUsers, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Цитаты из книги'


class ObjectiveYear(models.Model):  # "Цель на количество книг в год"
    goal_year = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Цель на год'
        verbose_name_plural = 'Цели на год'

    def __str__(self):
        return str(self.goal_year)


class ObjectiveReadingBook(models.Model):  # "Цель на дату к которой нужно дочитать книгу"
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    goal_read_book = models.DateField('Закончить к ')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Цель по книге'
        verbose_name_plural = 'Цели по книгам'

    def __str__(self):
        return f'{self.user.username} {self.book.title} К {self.goal_read_book}'


class BookReview(models.Model):  # "Оценка книги после прочтения, и отзыв на неё"
    title = models.CharField('Заголовок', max_length=155)
    text = models.TextField('Мои мысли о книге')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    rating = models.IntegerField('Оценка')

    class Meta:
        verbose_name = 'Рецензия'
        verbose_name_plural = 'Рецензии'

    def __str__(self):
        return self.title
