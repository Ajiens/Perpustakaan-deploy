from django.db import models
from django.contrib.auth.models import User

class Pengunjung(models.Model):
    pengunjung = models.ForeignKey(User, on_delete=models.CASCADE)
    is_member = models.BooleanField()

    
# Create your models here.
