from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.urls import reverse
from book.models import Book

def add_to_wishlist(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    wishlist = request.session.get('wishlist', [])
    
    if book.id not in wishlist:
        wishlist.append(book.id)
        request.session['wishlist'] = wishlist
        messages.info(request, 'The book was added to your temporary wishlist')
    else:
        messages.info(request, 'The book is already in your temporary wishlist')
    
    return HttpResponseRedirect(reverse('wishlist'))

def wishlist_view(request):
    wishlist = request.session.get('wishlist', [])
    books = Book.objects.filter(pk__in=wishlist)
    return render(request, 'wishlist.html', {'books': books})
