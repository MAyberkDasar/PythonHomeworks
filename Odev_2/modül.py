def bilgilendir():
    print("Merhaba ben Mehmet Ayberk DAŞAR, öğrenci numaram 211220006. Ben Python öğreniyorum ve fonksiyonlar ve modüllerle ilgili ödevimi yapıyorum.")

def stringeCevir(karakter):
    return str(karakter)

def harfMi(karakter):                                        # if(karakter >= "a" and karakter <= "z") or (karakter >= "A" and karakter <= "Z"):
    karakter = stringeCevir(karakter)                              # print("Girdiğiniz karakter bir harftir.")
    if(karakter.isalpha()):                                  # else:
        print("Girdiğiniz karakter bir harftir.")                  # print("Girdiğiniz karakter harf değildir.")
    else:                                                          
        print("Girdiğiniz karakter harf değildir.")                
                                                                                                                                        
def kücükHarfeCevir(karakter):
    karakter = stringeCevir(karakter)
    if(karakter.isupper()):
            karakter = karakter.lower()
            print(karakter)
    elif(karakter.islower()):
         print("Girdiğiniz harf zaten küçük harf.")
    else:
         print("Girdiğiniz karakter harf değildir.")
    
def frekansAnalizi(metin):
    metin = stringeCevir(metin)
    metin = metin.lower().replace(" ", "")
    harfler = []

    for harf in metin:
        if harf not in harfler and harf.isalpha():
            harfler.append(harf)

    for harf in sorted(harfler):
        adet = metin.count(harf)
        frekans = adet / len(metin) * 100
        print(f"{harf} harfinden {adet} adet var ve {harf} harfinin frekansı %{frekans:.2f}")

