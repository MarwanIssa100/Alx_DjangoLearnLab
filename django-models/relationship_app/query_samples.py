from models import Author, Book , Library, Librarian

def get_books_by_author(author_name):
    books = Book.objects.filter(author=author_name)
    return books

def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all() 
    return books

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian      
    return librarian