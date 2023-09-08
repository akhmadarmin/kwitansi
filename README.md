# Rupa-rupa python script
# Miscellanous
kwitansi.py
Pembuatan angka terbilang, cocok untuk kwitansi, ataupun invoice, dibuat dengan python native dan tersedia contoh penggunaan untuk django.
untuk cara penggunaan kwitansi.py sudah tinggal run biasa saja

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

maka Propinsi, Kota, Kelurahan dan KodePos akan tersalin dari wilayah.json ke models.py yang kamu buat