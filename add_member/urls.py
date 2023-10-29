from django.urls import path
from . import views

app_name = 'add_member'

urlpatterns = [
    path('add-member/', views.add_member, name='add-member'),
    path('karyawan/', views.karyawan_view, name='karyawan_view'),
    path('pelanggan/', views.pelanggan_view, name='pelanggan_view'),
]
