yasToplam = 0
ogrSayisi = int(input("Öğrenci Sayısı: "))
for sayac in range(1,ogrSayisi+1):
    print(sayac,".")
    ogrYas = int(input("öğrencinin Yaşı: "))
    yasToplam = yasToplam + ogrYas
ortalama = yasToplam/ogrSayisi
print(ortalama)
    





