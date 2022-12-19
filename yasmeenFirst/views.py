from django.shortcuts import render ,redirect
from yasmeenFirst import models

def addBook_index(request):
    books = models.get_all_book(request)
    context = {
        "books" : books
    }
    return render(request,'addBook.html',context)
# ----------------------------------------------------------------------
def addBook_method(request):
    if request.method == "POST":
        models.add_Book(request)
    return redirect('/')
# ----------------------------------------------------------------------
def addAuthor_index(request):
    authors = models.get_all_authors(request)
    context = {
        "authors" : authors
    }
    return render(request,"addAuthor.html",context)
# ----------------------------------------------------------------------
def addAuthor_method(request):
    if request.method == "POST":
        models.add_Author(request)
    return redirect("/add_author")
# ----------------------------------------------------------------------
def view_book(request):
    if request.method == "POST":
        id = models.view_book(request)
        author = models.get_all_authors(request)
        author_book = models.get_all_author_book(request)
        context = {
            "books" : id[0],
            "authors" : author,
            "author_book" : author_book
        }
    return render(request,'viewBook.html',context)
# ----------------------------------------------------------------------
def view_author(request):
    if request.method == "POST":
       id = models.view_Author(request)
       book = models.get_all_book(request)
       book_author = models.get_all_book_author(request)
       context ={
        "authors": id[0],
        "books": book,
        "book_author" : book_author
       }
       for boo in book:
            print(boo.title)
            print(boo.desc)
       print("************************")
    return render(request,'viewAuthor.html',context)
# ----------------------------------------------------------------------
def addBookToAuthor(request):
    if request.method == "POST":
        models.addBook_to_author(request)
    return redirect('/')

def addAutherToBook(request):
    if request.method == "POST":
        models.addAuthor_to_book(request)
    return redirect('/')



