from django.urls import path
from book.views import *

urlpatterns =[
    path("", get_books, name="get_books"),
    path("<int:id>/", get_books_id, name="get_books_id")
]