from django.shortcuts import render
from django.http import HttpResponseRedirect
from katalog_buku.forms import BookForm
from book.models import Book
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def show_main(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }

    # main = "";
    # if class pelanggan {
    #   main = main1.html
    # }
    # else if class karyawan {
    #   main = main2.html
    # }

    return render(request, "main1.html", context)


def add_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('katalog_buku:show_main'))

    context = {'form': form}
    return render(request, "add_book.html", context)


def show_xml(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")