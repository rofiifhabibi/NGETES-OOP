class KatakZuma:
    def __init__(self, warna_awal):
        self.warna_peluru = warna_awal
        self.skor = 0
        self.is_active = True
    
    def ganti_warna(self, warna_baru):
        self.warna_peluru = warna_baru

    def tembak(self):
        if self.is_active:
            self.skor += 50
        else:
            print("Katak tidak aktif, tidak bisa menembak.")
            
    def info_status(self):
        print(f"Warna Peluru: {self.warna_peluru}, Skor: {self.skor}, Aktif: {self.is_active}")


test = KatakZuma("merah")
test.info_status()

test.ganti_warna("hijau")
test.tembak()
test.info_status()  