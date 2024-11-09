from django.urls import path
from .views import LibraryDetailView , list_books

urlpatterns = [
    path('library/', LibraryDetailView.as_view(), name='library-detail'),
    path('list_books/', list_books, name='list_books'),
]