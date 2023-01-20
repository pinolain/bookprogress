from django import forms
from .models import Author, Book, Progres
from django.core.exceptions import ValidationError


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


class BookForm(forms.ModelForm):
    new_author = forms.CharField(max_length=155, label='Имя автора', required=False)
    #author = forms.ModelChoiceField(required=False, queryset=Author.objects.all())
    class Meta:
        model = Book
        fields = "__all__"

    def clean(self):
        data = super().clean()
        new_author = data.get('new_author')
        author = data.get('author')
        if new_author and author or not(new_author or author):
            raise ValidationError("Должно быть заполнинено только одно поле автор")
        return data



class ProgresForm(forms.ModelForm):
    class Meta:
        model = Progres
        exclude = ("user",)


class ProgresFormBook(forms.ModelForm):
    class Meta:
        model = Progres
        exclude = ("user", "book")
