from django.urls import path
from add_wishlist.views import *
from book.views import *

urlpatterns =[
    path("", wishlist_view, name='wishlist'),
    path("add/<int:book_id>/", add_to_wishlist, name="add"),
    path("remove/<int:book_id>/", remove_from_wishlist, name="remove"),
]