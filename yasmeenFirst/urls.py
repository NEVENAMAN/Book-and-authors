from django.urls import path
from . import views

urlpatterns = [
    path('',views.addBook_index),
    path('addBook_method',views.addBook_method),
    path('add_author',views.addAuthor_index),
    path('addAuthor_method',views.addAuthor_method),
    path('view_books',views.view_book),
    path('view_authors',views.view_author),
    path('addBookToAuthor',views.addBookToAuthor),
    path('addAutherToBook',views.addAutherToBook),
]