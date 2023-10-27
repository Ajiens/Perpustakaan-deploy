from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers


from book.models import Book

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_main(request):
    return render(request, "mainmain.html")

def get_buku_json(request):
    books = Book.objects.values()  # Mengambil semua data buku dari database
    return JsonResponse(list(books), safe=False)  # Mengirimkan daftar buku sebagai JSON

# def get_buku_json(request):
#     book = Book.objects.values().get(pk=1)  # Mengambil satu objek Book sebagai kamus
#     return JsonResponse(book, safe=False)

def deskripsi_buku(request, id):
    book = Book.objects.values().get(pk=id)
    return render(request, 'deskripsi.html', {'book':book})

def get_buku_json_by_id(request, id):
    book = Book.objects.values().get(pk=id)
    return JsonResponse(book, safe=False)
# Untuk ngambil semua data di database

