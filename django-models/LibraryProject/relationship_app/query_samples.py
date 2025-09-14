from relationship_app.models import Author
from relationship_app.models import Book
from relationship_app.models import Library
from relationship_app.models import Librarian

# Query all books by a specific author, personal comments btw
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)


# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
all_books = library.books.all()

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)