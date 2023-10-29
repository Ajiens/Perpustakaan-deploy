from django.urls import path
from pinjam_buku.views import *
from book.views import *

app_name = 'pinjam_buku'

urlpatterns =[
    path("", show_borrow, name='pinjam_buku_show'),
    path('pinjam/<int:id>/', pinjam_buku_request, name='pinjam'),
    path("pinjam_buku/", pinjam_buku_ajax, name="pinjam_buku"),
    path("kembalikan/<int:id>/", kembalikan_buku, name="kembalikan_buku"),
    path('get_buku_json/<int:id>/', get_buku_json_by_id, name='get_buku_json_by_id'),
    path('available_books_json/', available_books_json, name='available_books_json'),
    path('get_objek_json/<int:id>/', get_objek_by_id, name='get_objek_by_id'),
    path('get_borrowed_books_json/', get_borrowed_buku_json, name='get_borrowed_buku_json'),
]
