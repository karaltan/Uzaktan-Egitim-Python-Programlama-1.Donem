# İndeks/İndis kullanımı
""" Liste içindeki elemanlara erişmek için ilgili elemanın indeksi kullanılır.
Bazı kaynaklarda indis olarak da karşınıza çıkabilir. Köşeli parantez içine yazılır!!!
İlk elemanın indisi her zaman 0 (sıfır) olarak kabul edilir!!!."""

sehirler=["Ankara", "Bursa", "Çanakkale", "Denizli", "Eskişehir"]
# toplam 5 eleman var, sıraları= 0,1,2,3,4

# İlk elemanı ekrana yazdırınız.
print(sehirler[0]) # dikkat. ilk indisin değeri SIFIR(0)'dır. Ankara yazar

# İndeksi 2 olan elemanı ekrana yazdırınız.
print(sehirler[2]) # Çanakkale yazar

# Son elemanı yazdırınız
print(sehirler[4]) # Eskişehir yazar

print(sehirler[5]) # IndexError: list index out of range hatası verir