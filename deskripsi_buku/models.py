from django.db import models

from book.models import Book as Buku
from django.contrib.auth.models import User
# Create your models here.

class Review(models.Model):
    book = models.ForeignKey(Buku, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    komentar = models.TextField()
    rating_user = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)