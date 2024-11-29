from rest_framework import routers
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import path

router = routers.DefaultRouter()
router.register(r'books', ListView, basename='books')
router.register(r'books/<int:pk>', DetailView, basename='books_detail')
router.register(r'books/create', CreateView, basename='create')
router.register(r'books/update/<int:pk>', UpdateView, basename='update')
router.register(r'books/delete/<int:pk>', DeleteView, basename='delete')

urlpatterns = router.urls