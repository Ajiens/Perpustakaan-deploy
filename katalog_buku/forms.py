from django.forms import ModelForm
from main.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "cover_link", "rating_count", "harga"]