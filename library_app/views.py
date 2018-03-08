from django.shortcuts import render, get_object_or_404
from library_app.models import Category, Book, Publisher, Author
# Create your views here.

def home(request):
    book_categories = Category.objects.all()
    return render(request, 'home.html', {'categories':book_categories})

def book_list_in_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'library_app/books.html', {'category':category})

from django.views import generic

class CategoryListView(generic.ListView):
    model = Category

class CategoryDetailView(generic.DetailView):
    model = Category

class PublisherListView(generic.ListView):
    model = Publisher

class PublisherDetailView(generic.DetailView):
    model = Publisher

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author
