from django.shortcuts import render, redirect
from .forms import MemberForm
from .models import Member

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.save()
            # Logic buat promo klo pelanggannya member
            return redirect('nama_app:home')  # Ganti 'nama_app:home' dengan URL halaman setelah mendaftar member
    else:
        form = MemberForm()
    return render(request, 'add_member.html', {'form': form})
