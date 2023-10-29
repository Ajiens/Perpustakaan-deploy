from django.db import models
from django.contrib.auth.models import User
from book.models import Book
# Create your models here.

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    telephone_number = models.CharField(max_length=20)  
    email_address = models.EmailField()  
    duration_days = models.PositiveIntegerField()  
