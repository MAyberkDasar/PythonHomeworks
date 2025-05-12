"""
adet = 0
metin = input("Frekans analizi yapılacak metni giriniz: ")

for harf in metin: 
        adet=metin.count(harf)
        frekans = adet / len(metin)
        print(f"{harf} harfinden {adet} adet var ve {harf} harfinin frekansı {frekans}")
"""

harfler = []
metin = input("Frekans analizi yapılacak metni giriniz:").lower().replace(" ","")
print(len(metin))

for harf in metin[:100]:        
    if harf in harfler:
       continue
    elif harf.isalpha():
        harfler.append(harf)

print(harfler)        
    
for harf2 in sorted(harfler):
     adet = metin[:100].count(harf2)     
     print(f"{harf2} harfinden {adet} adet var ve {harf2} harfinin frekansı {adet/len(metin)*100}")

###################################################################################################
     
for harf in metin[:1000]:        
    if harf in harfler:
       continue
    elif harf.isalpha():
        harfler.append(harf)

print(harfler)        
    
for harf2 in sorted(harfler):
     adet = metin[:1000].count(harf2)     
     print(f"{harf2} harfinden {adet} adet var ve {harf2} harfinin frekansı {adet/len(metin)*100}")

###################################################################################################          
      
for harf in metin[:10000]:        
    if harf in harfler:
       continue
    elif harf.isalpha():
        harfler.append(harf)

print(harfler)        
    
for harf2 in sorted(harfler):
     adet = metin[:10000].count(harf2)     
     print(f"{harf2} harfinden {adet} adet var ve {harf2} harfinin frekansı {adet/len(metin)*100}")