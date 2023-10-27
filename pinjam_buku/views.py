from django.shortcuts import render
from book.models import Book
from pinjam_buku.models import Pelanggan
# Create your views here.

def pinjam_buku(request):
    if request.method == 'POST':
        book_id = request.POST.get(book_id)
        book = Book.objects.get(pk = book_id)

        #jika buku available gimana, nanti availablenya jadi false
    return -1

def kembalikan_buku(request):
    if request.method == 'POST':
        book_id = request.POST.get(book_id)
        book = Book.objects.get(pk = book_id)

        #available nya jadi true lagi
    return -1

