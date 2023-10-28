import datetime
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from pinjam_buku.models import Borrow
from book.models import Book

def available_books(request):
    available_books = Book.objects.filter(is_available=True)
    return render(request, 'available_books.html', {'available_books': available_books})

def get_borrowed_buku_json(request):
    borrowed_books = Borrow.objects.filter(user=request.user, return_date__isnull=True)
    return HttpResponse(serializers.serialize('json', borrowed_books))

def show_borrow(request):
    user = request.user
    borrowed_books = Borrow.objects.filter(user=user, return_date__isnull=True)
    return render(request, 'main_pinjam.html', {'borrowed_books': borrowed_books})

def pinjam_buku(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=book_id)
        telephone_number = request.POST.get("telephone_number")
        email_address = request.POST.get("email_address")
        duration_days = request.POST.get("duration_days")

        if book.is_available and telephone_number and email_address and duration_days:
            borrow_date = datetime.date.today()  # Tanggal peminjaman
            duration_days = int(duration_days)  # Mengubah durasi peminjaman menjadi integer
            return_date = borrow_date + datetime.timedelta(days=duration_days)  # Menghitung tanggal pengembalian
            borrow = Borrow(book=book, user=request.user, telephone_number=telephone_number, email_address=email_address, return_date=return_date)
            borrow.save()

            book.is_available = False
            book.save()
            return JsonResponse({'status': 'success', 'message': 'Buku berhasil dipinjam.'}, status=201)
        else:
            return JsonResponse({'status': 'error', 'message': 'Buku tidak tersedia untuk dipinjam atau informasi kontak tidak valid.'}, status=400)
    return HttpResponseNotFound()


def kembalikan_buku(request, borrow_id):
    borrow = get_object_or_404(Borrow, pk=borrow_id)
    book = borrow.book
    book.is_available = True
    book.save()
    borrow.return_date = datetime.date.today()
    borrow.save()

    return HttpResponseRedirect(reverse('pinjam_buku:show_borrow'))


