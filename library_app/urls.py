from django.urls import path
from library_app import views

urlpatterns = [
    path('<int:pk>/', views.book_list_in_category, name = "book_list"),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
	path('publishers/', views.PublisherListView.as_view(), name='publishers'),
	path('publisher/<int:pk>', views.PublisherDetailView.as_view(), name='publisher-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
	path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('books/', views.BookListView.as_view(), name='books'),
	path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]