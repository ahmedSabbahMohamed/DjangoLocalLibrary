from django.shortcuts import render
from django.views import generic
from .models import Book, Author

from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_author = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visists'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_author,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    context_object_name = 'book_list'
    queryset = Book.objects.all()
    template_name = 'books.html'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 1
    context_object_name= 'author_list'
    queryset = Author.objects.all()
    template_name = 'authors.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'
