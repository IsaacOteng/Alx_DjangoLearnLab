from django.urls import path
from .views import BookList
from api import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name="book_list_create"),
]
