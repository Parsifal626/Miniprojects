from django import template
from catalog.models import Book, Author

register = template.Library()

@register.simple_tag
def show_book():
    book = Book.objects.all()
    return book


@register.simple_tag
def show_authors():
    authors = Author.objects.all()
    return authors