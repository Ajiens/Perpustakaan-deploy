from django.forms import ModelForm
from pinjam_buku.models import Borrow

class BorrowForm(ModelForm):
    class Meta:
        model = Borrow
        fields = ["telephone_number","email_address", "duration_day"]