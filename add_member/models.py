from django.db import models

class Member(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role_choices = [
        ('customer', 'Pelanggan'),
        ('employee', 'Karyawan'),
    ]
    role = models.CharField(max_length=10, choices=role_choices)
    status_choices = [
        ('member', 'Member'),
        ('non_member', 'Non-Member'),
    ]
    status = models.CharField(max_length=10, choices=status_choices)

    def __str__(self):
        return self.username
