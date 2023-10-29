from django.urls import path
from main.views import *

urlpatterns =[
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]