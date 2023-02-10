from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from booktracker.api.serializer import AuthorSerializer, BookSerializer, BookDetailSerializer, ProgressSerializer, AttachmentSerializer
from booktracker.models import Author, Book, Progres, Attachment


class AuthorListCreateApiView(ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = (IsAuthenticated,)


class BookListView(ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()


class ProgressReadView(ListCreateAPIView):
    serializer_class = ProgressSerializer
    def get_queryset(self):
        return Progres.objects.filter(user_id=1, book_id=self.kwargs['book_id'])

    def perform_create(self, serializer):
        if not serializer.validated_data.get('start_page'):
            serializer.save(user_id=1, book_id=self.kwargs['book_id'], start_page= self.get_start_page(self.kwargs['book_id'], 1))
        else:
            serializer.save(user_id=1, book_id=self.kwargs['book_id'])

    def get_start_page(self, book_id, user_id):
        print(self)

        last_progres = Progres.objects.filter(book_id=book_id, user_id=user_id).order_by('-end_time').first()
        if last_progres:
            return last_progres.end_page

        return 0


class ProgressEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProgressSerializer
    queryset = Progres.objects.all()


class AttachmentView(ListCreateAPIView):
    serializer_class = AttachmentSerializer
    queryset = Attachment.objects.all()
