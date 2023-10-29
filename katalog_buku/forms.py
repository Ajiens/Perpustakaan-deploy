from django.forms import ModelForm
from katalog_buku.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "cover_link", "harga"]