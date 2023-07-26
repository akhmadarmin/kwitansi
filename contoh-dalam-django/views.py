from django.shortcuts import render
from invoice.terbilang import Kwitansi

def kwitansi(request):
    if request.method == 'POST':
        angka_input = request.POST.get('angka_input')  # ganti 'angka_input' dengan name di template
        kwitansi = Kwitansi()
        terbilang_angka = kwitansi.terbilang(angka_input)

        context = {
            'angka_input': angka_input,
            'terbilang_angka': terbilang_angka,
            'user': user_login, #sesuaikan, biasanya ada instance user_login = User.objects.get(user=request.user)
        }
    
        return render(request, 'contoh_template.html', context)  
	return render(request, 'contoh_template.html')