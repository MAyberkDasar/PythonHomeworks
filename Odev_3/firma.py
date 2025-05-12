
class Firma():
    def __init__(self):
        self.personelListesi = []

    def personelEkle(self, personel):
        self.personelListesi.append(personel)

    def personelListele(self):
        for personel in self.personelListesi:
            print("Adı: ", personel.ad)
            print("Departmanı:", personel.departman)
            print("Çalışma Yılı:", personel.yil)
            print("Maaşı:", personel.maas)

    def maasZammı(self, personel, zamOrani):
        personel.maas += (personel.maas * zamOrani / 100)
    
    def personelCikart(self, personel):
        self.personelListesi.remove(personel)
