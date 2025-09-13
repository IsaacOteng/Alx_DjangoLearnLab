book = Books.objects.create(title="1984", author="George Orwell", publication_year=1949)

book
<Book: 1984 by George Orwell>book = Book.objects.get(title="1984")  

book.title, book.author, book.publication_year
('Ninteen Eighty-Four', 'George Orwell', 1949)book.title = "Ninteen Eighty-Four"
book.save()
book.title

'Ninteen Eighty-Four'book.delete()

Book.objects.all()
<QuerySet []>