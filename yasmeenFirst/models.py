from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=60)
    desc = models.TextField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# -----------------------------------------------------------
def get_all_book(request):
    return Book.objects.all()

def get_all_authors(request):
    return Author.objects.all()

def get_all_book_author(request):
    id = request.POST['authorID']
    this_author = Author.objects.get(id = id)
    books = this_author.books.all()
    return books

def get_all_author_book(request):
    id= request.POST['bookID']
    this_book = Book.objects.get(id = id)
    return this_book.authors.all()
# ----------------------------------------------------
def add_Book(request):
    title = request.POST['title']
    description = request.POST['description']
    return Book.objects.create(title = title , desc = description)

def add_Author(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes = request.POST['notes']
    return Author.objects.create(first_name = first_name , last_name = last_name , notes = notes)
# -----------------------------------------------------------
def view_Author(request):
    print("*****")
    id = request.POST['authorID']
    return Author.objects.filter(id = id)

def view_book(request):
    id = request.POST['bookID']
    return Book.objects.filter(id = id)
# -----------------------------------------------------------
def addBook_to_author(request):
    book = request.POST['selectBook']
    author = request.POST['author_id']
    book_id = Book.objects.get(id = book)
    author_id = Author.objects.get(id = author)
    book_id.authors.add(author_id)
    author_id.books.add(book_id)
    
def addAuthor_to_book(request):
    author = request.POST['selectauthor']
    book = request.POST['book_id']
    author_id= Author.objects.get(id=author)
    book_id= Book.objects.get(id=book)
    author_id.books.add(book_id)
    book_id.authors.add(author_id)
