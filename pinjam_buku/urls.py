from django.urls import path
from pinjam_buku.views import *
from book.views import *

app_name = 'pinjam_buku'

urlpatterns =[
    path("", show_borrow, name='pinjam_buku'),
    path("pinjam_buku/<int:book_id>/", pinjam_buku, name="pinjam_buku"),
    path("kembalikan/<int:borrow_id>/", kembalikan_buku, name="kembalikan_buku"),
]