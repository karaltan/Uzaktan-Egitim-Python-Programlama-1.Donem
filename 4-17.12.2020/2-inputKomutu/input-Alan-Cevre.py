"""Kullanıcının girdiği kısa ve uzun kenar değerlerine göre 
dikdörtgenin alanını ve çevresini hesaplayınız.
Daha sonra Dikdörtgenin Alanı: ….. Çevresi:……. şeklinde bir çıktı üretiniz"""

kisa=int(input("dikdörtgenin kısa kenarını giriniz:"))
uzun=int(input("dikdörtgenin uzun kenarını giriniz:"))

alan=kisa*uzun
#cevre=kisa+uzun+kisa+uzun
cevre=2*(kisa+uzun)

print("alan=",alan)
print("çevre=",cevre)