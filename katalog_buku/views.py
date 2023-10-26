from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import BookForm
from main.models import Book
from django.urls import reverse

# Create your views here.

def show_main(request):
    books = Book.objects.all()

    context = {
        'name': 'Purrfect Pages',
        'class': 'PBP E',
        'books': books,
    }

    return render(request, "main.html", context)

def add_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "add_book.html", context)