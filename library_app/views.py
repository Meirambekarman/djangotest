from django.shortcuts import render, get_object_or_404
from library_app.models import Category, Book, Publisher, Author
import datetime
# Create your views here.

def home(request):
    book_categories = Category.objects.all()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    time = datetime.datetime.now()
    w_day = time.weekday()
    day = time.day
    month = time.month
    year = time.year
    microsecond = time.microsecond
    second = time.second
    minute = time.minute
    hour = time.hour

    return render(request, 'home.html', {'categories':book_categories,'num_visits':num_visits, 'weekday': w_day,
                 'hour': hour, 'minute': minute, 'second': second, 'microsecond': microsecond,
                 'day': day, 'month': month, 'year': year})  # num_visits appended

def book_list_in_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'library_app/books.html', {'category':category})

from django.views import generic

class CategoryListView(generic.ListView):
    model = Category
    paginate_by = 2

class CategoryDetailView(generic.DetailView):
    model = Category

class PublisherListView(generic.ListView):
    model = Publisher
    paginate_by = 2

class PublisherDetailView(generic.DetailView):
    model = Publisher

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2

class AuthorDetailView(generic.DetailView):
    model = Author
