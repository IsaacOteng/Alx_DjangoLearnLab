from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic.list import ListView
from .models import Library
from .models import Book


# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryListView(ListView):
    model = Library
    template_name = 'relationship_app/library_list.html'
    context_object_name = 'libraries'