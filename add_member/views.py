from django.http import HttpResponseRedirect
from .forms import MemberForm
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Member
from book.models import Book, Borrow, Wishlist, Review

@login_required
def karyawan_view(request):
    try:
        member = Member.objects.get(username=request.user.username, role='employee')
        pelanggan_list = Member.objects.filter(role='customer')
        history_peminjaman = Borrow.objects.all()
        daftar_wishlist = Wishlist.objects.all()

        context = {
            'pelanggan_list': pelanggan_list,
            'history_peminjaman': history_peminjaman,
            'daftar_wishlist': daftar_wishlist,
        }

        return render(request, 'add_member/karyawan.html', context)
    except Member.DoesNotExist:
        # Pengguna bukan karyawan atau tidak ada Member dengan peran 'employee'
        return render(request, 'add_member/error.html', {'error_message': 'Anda tidak memiliki akses sebagai karyawan.'})

@login_required
def pelanggan_view(request):
    try:
        member = Member.objects.get(username=request.user.username, role='customer')
        katalog_buku = Book.objects.all()

        if request.method == 'POST':
            action = request.POST.get('action')
            book_id = request.POST.get('book_id')
            book = Book.objects.get(pk=book_id)

            if action == 'pinjam':
                if book.is_available:
                    borrow = Borrow(book=book, user=request.user, telephone_number=member.telephone_number, email_address=member.email, duration_days=7)
                    borrow.save()

                    book.is_available = False
                    book.save()

                    messages.success(request, f"Buku {book.title} berhasil dipinjam.")
                else:
                    messages.error(request, f"Buku {book.title} tidak tersedia untuk dipinjam.")

            elif action == 'wishlist':
                wishlist = Wishlist(book=book, user=request.user)
                wishlist.save()

                messages.success(request, f"Buku {book.title} ditambahkan ke wishlist.")

            elif action == 'review':
                rating = request.POST.get('rating')
                comment = request.POST.get('comment')

                review = Review(book=book, user=request.user, rating=rating, comment=comment)
                review.save()

                messages.success(request, "Review Anda telah ditambahkan.")
            return redirect('pelanggan_view')

        context = {
            'katalog_buku': katalog_buku,
        }

        return render(request, 'add_member/pelanggan.html', context)
    except Member.DoesNotExist:
        return render(request, 'add_member/error.html', {'error_message': 'Anda tidak memiliki akses sebagai pelanggan.'})
