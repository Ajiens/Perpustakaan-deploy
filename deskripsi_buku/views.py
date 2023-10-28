from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from pengunjung.models import Pengunjung
from book.models import Book
from deskripsi_buku.models import Review

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
    print(request.user.id)
    pengunjung = Pengunjung.objects.values().get(pengunjung_id=request.user.id)
    book = Book.objects.values().get(pk=id)
    print(pengunjung, " + ")
    return render(request, 'deskripsi.html', {'book':book})

def review_buku(request, id):
    book = Book.objects.values().get(pk=id)
    review = Review.objects.values().all()
    context = {
        'book':book,
        'reviews': list(review),
    }
    return render(request, 'review.html', context)

@login_required(login_url='/login')
@csrf_exempt
def add_review_buku(request):
    print(request.POST.get("komentar"), request.POST.get("rating"))
    if request.method == 'POST':
        komentar = request.POST.get("komentar")
        rating = request.POST.get("rating")
        user = request.user
        book = Book.objects.get(pk=int(request.POST.get("buku_id")))

        if int(rating) == 5:
            book.five_star_ratings += 1
        elif int(rating) == 4:
            book.four_star_ratings += 1
        elif int(rating) == 3:
            book.three_star_ratings += 1
        elif int(rating) == 2:
            book.two_star_ratings += 1
        elif int(rating) == 1:
            book.one_star_ratings += 1
        else:
            return HttpResponseNotFound()
        # ((Overall Rating * Total Rating) + new Rating) / (Total Rating + 1)
        new_rating = ((book.average_rating * book.rating_count) + int(rating)) / (book.rating_count + 1)
        book.average_rating = round(new_rating,2)
        book.rating_count += 1
        book.save()
         

        new_review = Review(book=book, user=user, rating_user=rating, komentar=komentar)
        new_review.save()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

def get_review(request):
    # review = Review.objects.values()
    review = Review.objects.values()
    return JsonResponse(list(review), safe=False)
    # return HttpResponse(serializers.serialize("json", review), content_type="application/json")


def get_buku_json_by_id(request):
    book = Book.objects.values().get(pk=int(request.GET.get("book_id")))
    # print("Inidia nih si buku ID:",book)
    # return HttpResponse(serializers.serialize("json", book), content_type="application/json")
    return JsonResponse(book, safe=False)

# Untuk ngambil semua data di database

