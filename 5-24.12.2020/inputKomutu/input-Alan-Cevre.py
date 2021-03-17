"""Kullanıcının girdiği kısa ve uzun kenar değerlerine göre 
dikdörtgenin alanını ve çevresini hesaplayınız.
Daha sonra Dikdörtgenin Alanı: ….. Çevresi:……. şeklinde bir çıktı üretiniz"""

#giriş
kisa=int(input("dikdörtgenin kısa kenarını giriniz:"))
uzun=int(input("dikdörtgenin uzun kenarını giriniz:"))

#gelişme
alan=kisa*uzun
#cevre=kisa+uzun+kisa+uzun
cevre=2*(kisa+uzun)

#sonuç
print("alan=",alan)
print("çevre=",cevre)

print("Alan : {0}".format(alan))
print("Çevre : {0}".format(cevre))
