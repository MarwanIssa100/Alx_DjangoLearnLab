from django.urls import path
from .views import LibraryDetailView , book_list

urlpatterns = [
    path('library/', LibraryDetailView.as_view(), name='library-detail'),
    path('book_list/', book_list, name='book-list'),
]