import os
import django
from django.db import transaction

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nama_project.settings')
django.setup()

from wilayah.models import Wilayah
from harta_benda.models import Propinsi, Kota, Kelurahan, KodePos

def import_data():
    wilayah_data = Wilayah.objects.all()
    chunk_size = 500

    bulk_propinsi = []
    bulk_kota = []
    bulk_kelurahan = []
    bulk_kode_pos = []

    for i, wilayah in enumerate(wilayah_data, 1):
        propinsi_name = wilayah.propinsi
        kota_name = wilayah.kota
        kelurahan_name = wilayah.kelurahan
        kode_pos_value = wilayah.kode_pos

        propinsi, _ = Propinsi.objects.get_or_create(nama_propinsi=propinsi_name)
        kota, _ = Kota.objects.get_or_create(nama_kota=kota_name, propinsi=propinsi)
        kelurahan, _ = Kelurahan.objects.get_or_create(nama_lurah=kelurahan_name, kode_pos=kode_pos_value, kota=kota)
        kode_pos, _ = KodePos.objects.get_or_create(kode_pos=kode_pos_value, nama_lurah=kelurahan)

        bulk_propinsi.append(propinsi)
        bulk_kota.append(kota)
        bulk_kelurahan.append(kelurahan)
        bulk_kode_pos.append(kode_pos)

        if i % chunk_size == 0:
            with transaction.atomic():
                Propinsi.objects.bulk_create(bulk_propinsi)
                Kota.objects.bulk_create(bulk_kota)
                Kelurahan.objects.bulk_create(bulk_kelurahan)
                KodePos.objects.bulk_create(bulk_kode_pos)

            bulk_propinsi.clear()
            bulk_kota.clear()
            bulk_kelurahan.clear()
            bulk_kode_pos.clear()

    with transaction.atomic():
        Propinsi.objects.bulk_create(bulk_propinsi)
        Kota.objects.bulk_create(bulk_kota)
        Kelurahan.objects.bulk_create(bulk_kelurahan)
        KodePos.objects.bulk_create(bulk_kode_pos)

if __name__ == '__main__':
    import_data()