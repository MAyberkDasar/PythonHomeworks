from firma import Firma
from personel import Personel


firma1 = Firma()

personel1 = Personel("Fatma", "Muhasebe", 3, 15000)
personel2 = Personel("Ayşe", "İnsan Kaynakları", 2, 17000)
personel3 = Personel("Ahmet", "Satış", 5, 16000)
personel4 = Personel("Mehmet","Yazılım",10,20000)

firma1.personelEkle(personel1)
firma1.personelEkle(personel2)
firma1.personelEkle(personel3)
firma1.personelEkle(personel4)

print(firma1.personelListele())

print("********************")

firma1.maasZammı(personel1,10)
firma1.maasZammı(personel2,5)
firma1.maasZammı(personel3,15)
firma1.maasZammı(personel4,20)

print(firma1.personelListele())

print("********************")

firma1.personelCikart(personel3)

print(firma1.personelListele())



