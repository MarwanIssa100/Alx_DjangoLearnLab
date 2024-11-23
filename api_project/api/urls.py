from django.urls import path , include
from rest_framework.routers.urls import include
from .views import BookList , BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books', BookViewSet , basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  
]