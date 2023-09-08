# Rupa-rupa python script
# Miscellanous buat kalau mau pakai tinggal comot yang udah ketulis

kwitansi.py
Pembuatan angka terbilang, cocok untuk kwitansi, ataupun invoice, dibuat dengan python native dan tersedia contoh penggunaan untuk django.
untuk cara penggunaan kwitansi.py sudah tinggal run biasa saja

============================

copy_antar_tabel.py 

adalah tools buat copy file wilayah.json dimana file wilayah.json tersebut 
(untuk wilayah.json saya copy dari https://github.com/drizki/geografis)
berisi nama Propinsi nama Kota nama Kecamatan nama Kelurahan hingga no Kode Pos seluruh Indonesia.

Tapi yang saya ambil hanya Propinsi, Kota, Kelurahan dan KodePos saja.
Saya gunakan saat menampilkan seluruh nama kota, kelurahan dan kode pos se Indonesia 
untuk project Asuransi.

cara penggunaan copy_antar_tabel.py, sederhana saja
buat tabel di models.py dengan fields yang sesuai
ubah nama_project.settings menjadi project_django_kamu.settings
letakkan di folder terluar django bersamaan 1 directory dengan requirements.txt
lalu run di terminal dalam env seperti biasa.

maka Propinsi, Kota, Kelurahan dan KodePos akan tersalin dari wilayah.json ke models.py yang dibuat 

============================

atur.py 

Adalah group_required untuk fungsi decorator, karena saya biasa pakai 
FBV atau Function Based Views, sehingga gak pake LoginRequiredMixin.

Ref :
https://codereview.stackexchange.com/questions/57073/django-custom-decorator-for-user-group-check
https://dmitry-naumenko.medium.com/how-to-create-a-decorator-for-checking-groups-in-django-40a9df327c4b

pakai *group_names biar sebagai tuple, biar lebih dari satu user group.

Pastinya harus buat group user dari django admin dulu.
kalau saya taruh di directory project, jadi pas mau pakai taruh di views, tinggal pakai : 

from nama_projects.atur import group_required 

@group_required('Group 1', 'Group 2')
def nama_views(request):
	pass 
	
seperti itu.....

==============================