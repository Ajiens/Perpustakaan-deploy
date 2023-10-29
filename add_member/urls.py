from django.urls import path
from add_member.views import * 

app_name = 'add_member'

urlpatterns = [
    path('', add_member, name='add-member'),
    path('karyawan/', karyawan_view, name='karyawan_view'),
    path('pelanggan/', pelanggan_view, name='pelanggan_view'),
]