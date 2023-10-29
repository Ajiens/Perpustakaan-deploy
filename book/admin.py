from django.contrib import admin

from .models import Book
from deskripsi_buku.models import Review

myModels = [Book, Review]  # iterable list
admin.site.register(myModels)
# Register your models here.
