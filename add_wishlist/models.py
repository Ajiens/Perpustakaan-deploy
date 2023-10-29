from django.db import models
from django.contrib.auth.models import User
from book.models import Book  # Mengimport model Book yang sudah ada

class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wished_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # slug = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.wished_book.title