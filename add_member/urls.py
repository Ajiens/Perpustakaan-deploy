from django.urls import path
from . import views

app_name = 'add_member'

urlpatterns = [
    path('add-member/', views.add_member, name='add-member'),
]
