from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from book.models import Book


# Create your views here.

def show_main(request):
    return render(request, "main.html")

def pelanggan_view(request):
    return render(request, 'pelanggan.html')

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_buku_json(request):
    books = Book.objects.values()  # Mengambil semua data buku dari database
    return JsonResponse(list(books), safe=False)  # Mengirimkan daftar buku sebagai JSON


def deskripsi_buku(request, id):
    book = Book.objects.values().get(pk=id)
    return render(request, 'deskripsi.html', {'book':book})

def get_buku_json_by_id(request, id):
    book = Book.objects.values().get(pk=id)
    return JsonResponse(book, safe=False)
