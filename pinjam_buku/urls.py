from django.urls import path
from pinjam_buku.views import *
from book.views import *

app_name = 'pinjam_buku'

urlpatterns =[
    path("", show_borrow, name='pinjam_buku_show'),
    path('pinjam/<int:id>/', pinjam_buku_request, name='pinjam'),
    path("pinjam_buku/", pinjam_buku, name="pinjam_buku"),
    path("kembalikan/<int:borrow_id>/", kembalikan_buku, name="kembalikan_buku"),
]