import sqlite3

def jaccard(metin1,metin2):
    küme1 = set(metin1)
    küme2 = set(metin2)

    kesisim = len(küme1.intersection(küme2))
    birlesim = len(küme1.union(küme2))

    benzerlikKatsayisi1 = kesisim / birlesim

    return benzerlikKatsayisi1

def sorensenDice(metin1,metin2):
    metin1 = set(metin1)
    metin2 = set(metin2)

    benzerlikKatsayisi2 = (2 * len(metin1.intersection(metin2))) / (len(metin1) + len(metin2))

    return benzerlikKatsayisi2


baglan = sqlite3.connect("metinler.db") # Veritabanına bağlanıldı.

imlec = baglan.cursor() # İmleç oluşturuldu.

metin1 = input("Metin giriniz: ")
metin2 = input("Metin giriniz: ")

imlec.execute("CREATE TABLE IF NOT EXISTS metinler(metin TEXT)") # Tablo oluşturuldu.

imlec.execute("INSERT INTO metinler VALUES(?)",(metin1,)) # Metin1 değişkeni tabloya eklendi.
imlec.execute("INSERT INTO metinler VALUES(?)",(metin2,)) # Metin2 değişkeni tabloya eklendi.

baglan.commit() # Veritabanı güncellendi.

imlec.execute("SELECT * FROM metinler") # Sorgu yapıldı.

print(imlec.fetchall()) # Ekrana metinler bastırıldı.

print(f"Jaccard: {jaccard(metin1,metin2)}")
print(f"Sorensen Dice: {sorensenDice(metin1,metin2)}")

benzerlikSonuclari = [f"Jaccard: {jaccard(metin1,metin2)}\n" , f"Sorensen Dice: {sorensenDice(metin1,metin2)}"]

with open("benzerlik_durumu.txt","w") as file: # Dosya write modunda açıldı.
    file.writelines(benzerlikSonuclari) # Dosyaya yazdırıldı.

imlec.execute("DELETE FROM metinler") # Tablo temizlendi.

baglan.commit() # Veritabanı güncellendi.

baglan.close() # Bağlantı kesildi.