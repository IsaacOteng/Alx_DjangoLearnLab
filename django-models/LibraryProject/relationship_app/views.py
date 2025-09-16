from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class register(CreateView):
    form_class = UserCreationForm
    template_name = "relationship_app/register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # logs in for this session
        return redirect("profile")
    
