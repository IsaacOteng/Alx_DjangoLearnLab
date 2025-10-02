from django.contrib import admin
from django.urls import path
from api.views import BookCreateView, BookDetailView, BookDeleteView, BookListView, BookUpdateView


urlpatterns = [
    path('books/', BookListView.as_view(), name= 'books'),
    path('books/<int:pk>/detail/', BookDetailView.as_view(), name= 'books'),
    path('books/create', BookCreateView.as_view(), name= 'books'),
    path('books/update', BookUpdateView.as_view(), name= 'books'),
    path('books/delete', BookDeleteView.as_view(), name= 'books'),
]
