from rest_framework import serializers
from booktracker.models import Author, Book, Progres, Attachment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class ProgressSerializer(serializers.ModelSerializer):
    start_page = serializers.IntegerField(required=False, label='Начальная страница')

    class Meta:
        model = Progres
        exclude = ('user', 'book',)


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ('text',)
