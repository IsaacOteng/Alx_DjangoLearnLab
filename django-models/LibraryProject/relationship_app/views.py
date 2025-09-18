from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from .forms import RegistrationForm


# User Roles 
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == "Admin"

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == "Librarian"

def is_member(user):
    return user.is_authenticated and user.userprofile.role == "Member"


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "member_view.html")

# Redirectiong Users Based On their roles
def role_redirect(request):

    if not request.user.is_authenticated:
        return redirect("register") 
    
    role = request.user.userprofile.role
    if role == "Admin":
        return redirect("admin_view")
    elif role == "Librarian":
        return redirect("librarian_view")
    else:
        return redirect("member_view")
    

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# class register(CreateView):
#     form_class = UserCreationForm
#     template_name = "relationship_app/register.html"

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)  # logs in for this session
#         return redirect("profile")

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("role_redirect")
        
    else:
        form = RegistrationForm()
    
    return render(request, "relationship_app/register.html", {"form": form})
