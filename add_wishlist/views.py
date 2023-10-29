from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.urls import reverse
from django.core import serializers
from book.models import Book

def add_to_wishlist(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    wishlist = request.session.get('wishlist', [])
    
    if book.id not in wishlist:
        wishlist.append(book.id)
        request.session['wishlist'] = wishlist
        success = True
    else:
        success = False

    return JsonResponse({'success': success})


def remove_from_wishlist(request, book_id):
    wishlist = request.session.get('wishlist', [])
    
    if book_id in wishlist:
        wishlist.remove(book_id)
        request.session['wishlist'] = wishlist
        success = True
    else:
        success = False

    return JsonResponse({'success': success})


def wishlist_view(request):
    wishlist = request.session.get('wishlist', [])
    books = Book.objects.filter(pk__in=wishlist)
    return render(request, 'wishlist.html', {'wishlist': books})


def get_books_json(request):
    wishlist = request.session.get('wishlist', [])
    books = Book.objects.filter(pk__in=wishlist).values()  # Filter hanya buku yang ada dalam wishlist
    return JsonResponse(list(books), safe=False)