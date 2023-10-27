from django.urls import path
from deskripsi_buku.views import *

app_name = 'deskripsi_buku'

urlpatterns =[
    path('', show_main, name='show_main'),
    path("daftar-buku-json/", show_json, name="get_books"),
    path('get_buku_json/', get_buku_json, name='get_buku_json'),
    path('json/<int:id>/', get_buku_json_by_id, name='show_json_by_id'),
    path('deskripsi/<int:id>/', deskripsi_buku, name="deskripsi")
]