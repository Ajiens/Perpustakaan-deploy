from django.forms import ModelForm
from katalog_buku.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "cover_link", "average_rating", "harga"]