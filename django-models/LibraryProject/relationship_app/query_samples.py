from relationship_app.models import Author
from relationship_app.models import Book
from relationship_app.models import Library
from relationship_app.models import Librarian


author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)

library_name = "Central Library"
library = Library.objects.get(name=library_name)
all_books = library.books.all()

librarian = Librarian.objects.get(name="Alice")
library_of_librarian = librarian.library



