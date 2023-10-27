from django.urls import path
from katalog_buku.views import show_main, add_book

app_name = 'katalog_buku'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-book/', add_book, name='add_book'),
]