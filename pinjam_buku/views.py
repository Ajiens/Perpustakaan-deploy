import datetime
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from pinjam_buku.models import Borrow
from book.models import Book
from django.views.decorators.csrf import csrf_exempt

def show_borrow(request):
    user = request.user
    borrowed_books = Borrow.objects.filter(user=user, return_date__isnull=True)
    return render(request, 'main_pinjam.html', {'borrowed_books': borrowed_books})

@csrf_exempt
def pinjam_buku_ajax(request):
    print("bencana")
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=request.POST.get("bookId"))
        telephone_number = request.POST.get("telephone_number")
        email_address = request.POST.get("email_address")
        duration_days = request.POST.get("duration_days")

        if book.is_available:
            borrow_date = datetime.date.today()  # Tanggal peminjaman
            duration_days = int(duration_days)  # Mengubah durasi peminjaman menjadi integer
            return_date = borrow_date + datetime.timedelta(days=duration_days)  # Menghitung tanggal pengembalian
            borrow = Borrow(book=book, user=request.user, telephone_number=telephone_number, email_address=email_address, return_date=return_date)
            borrow.save()

            book.is_available = False
            book.save()
            return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def kembalikan_buku(request, borrow_id):
    if request.method == 'POST':
        buku_dikembalikan = Book.objects.get(pk=id)
        buku_dikembalikan.is_available= True
        buku_dikembalikan.save()
        objekPeminjaman = Borrow.objects.filter(buku=buku_dikembalikan).filter(user=request.user)
        objekPeminjaman.first().delete()
        return HttpResponse(b"DIHAPUS", status = 201)
    return HttpResponseNotFound()    

def pinjam_buku_request(request, id):
    book = Book.objects.values().get(pk=id)
    return render(request, 'pinjam_buku.html', {'book':book})

def get_buku_json_by_id(request, id):
    book = Book.objects.values().get(pk=id)
    return JsonResponse(book, safe=False)

def available_books_json(request):
    available_books = Book.objects.filter(is_available=True)
    return HttpResponse(serializers.serialize('json', available_books))

def get_objek_by_id(request, id):
    cariPinjaman = Borrow.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', cariPinjaman))

def get_borrowed_buku_json(request):
    borrowed_books = Borrow.objects.filter(user=request.user, return_date__isnull=True)
    return HttpResponse(serializers.serialize('json', borrowed_books))
