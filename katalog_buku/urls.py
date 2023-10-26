from django.urls import path
from main.views import show_main, add_book
from django.urls import path, include

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('add-book', add_book, name='add_book'),
]