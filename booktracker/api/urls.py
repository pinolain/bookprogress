from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import AuthorListCreateApiView, BookListView, BookDetailView, ProgressReadView, ProgressEditView, AttachmentView

urlpatterns = [
    path('author/', AuthorListCreateApiView.as_view()),
    path('book/', BookListView.as_view()),
    path('book/<int:pk>', BookDetailView.as_view()),
    path('book/<int:book_id>/progress', ProgressReadView.as_view()),
    path('book/<int:book_id>/progress/edit', ProgressEditView.as_view()),
    path('lc/attachment', AttachmentView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]