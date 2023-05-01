from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, Genre, Language, Status, BookInstance
from django.views import generic
# Create your views here.

def index(request):
    # Генерация количеств некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Достпные книги (= "На складе")
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    #Авторы книг
    num_authors = Author.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session ["num_visits"] = num_visits + 1

    # Отрисовка HTML-шаблона index.html с данными
    # внутрии переменной context
    return render(request, "index.html",
                   context={"num_books": num_books,
                            "num_instances": num_instances,
                            "num_instances_available": 
                            num_instances_available,
                            "num_authors": num_authors,
                            "num_visits": num_visits},
                )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2


class AuthorListView(generic.ListView):
    model = Author
    

class BookDetailView(generic.DetailView):
    model = Book

class GenreListView(generic.ListView):
    model = Genre

class AuthorDetailView(generic.DetailView):
    model = Author
