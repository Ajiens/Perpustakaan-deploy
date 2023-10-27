from django.urls import path
from add_wishlist.views import *
from book.views import *

urlpatterns =[
    path("", wishlist_view, name='wishlist'),
]