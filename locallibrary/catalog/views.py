from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact=BookInstance.LoanStatus.AVAILABLE).count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    queryset = Book.objects.filter(title__icontains='crime')[:5]
    template_name = 'books/my_crime_list.html'

    def get_queryset(self):
        return Book.objects.filter(title__icontains='crime')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context

class BookDetailView(generic.DetailView):
    model = Book