#model membuat kwitansi untuk terbilang, pure python

class Kwitansi:
    def __init__(self):
        self.angka_terbilang = ""

    def terbilang(self, angka):
        angka = int(angka)
        if angka < 1 or angka >= 1000000000:
            return "Angka harus berada di antara 1 hingga 999.999.999"

        self.angka_terbilang = self._terbilang(angka)
        return self.angka_terbilang

    def _terbilang(self, angka):
        satuan = ["", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan"]
        belasan = ["", "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas", "enam belas", "tujuh belas", "delapan belas", "sembilan belas"]
        puluhan = ["", "sepuluh", "dua puluh", "tiga puluh", "empat puluh", "lima puluh", "enam puluh", "tujuh puluh", "delapan puluh", "sembilan puluh"]

        if angka < 10:
            return satuan[angka]
        elif angka < 20:
            return belasan[angka - 10]
        elif angka < 100:
            return puluhan[angka // 10] + " " + satuan[angka % 10]
        elif angka < 1000:
            if angka // 100 == 1:
                if angka % 100 == 0:
                    return "seratus " + self._terbilang(angka % 100)
                else:
                    return "seratus " + self._terbilang(angka % 100)
            else:
                return satuan[angka // 100] + " ratus " + self._terbilang(angka % 100)
        elif angka < 10000:
            return satuan[angka // 1000] + " ribu " + self._terbilang(angka % 1000)
        elif angka < 1000000:
            return self._terbilang(angka // 1000) + " ribu " + self._terbilang(angka % 1000)
        elif angka < 1000000000:
            if angka < 2000000:
                return "satu juta " + self._terbilang(angka % 1000000)
            elif angka < 100000000:
                if angka // 1000000 == 1:  
                    if angka % 1000000 == 0:  
                        return "seratus juta " + self._terbilang(angka % 1000000)
                    else:
                        return "seratus " + self._terbilang(angka % 1000000)
                else:
                    return satuan[angka // 1000000] + " juta " + self._terbilang(angka % 1000000)
            else:
                if angka // 1000000 == 1:  
                    if angka % 1000000 == 0:  
                        return "seratus juta " + self._terbilang(angka % 1000000)
                    else:
                        return "seratus " + self._terbilang(angka % 1000000)
                else:
                    return self._terbilang(angka // 1000000) + " juta " + self._terbilang(angka % 1000000)

kwitansi = Kwitansi()
angka = int(input('Ketik Angka : '))
terbilang_angka = kwitansi.terbilang(angka)
print(f"{angka:,} = {terbilang_angka}")

#cara pemanggilan diatas sudah dilakukan, cukup running script saja