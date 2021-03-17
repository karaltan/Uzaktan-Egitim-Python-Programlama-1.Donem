"""
Kullanıcının girdiği kısa ve uzun kenar değerlerine göre;
dikdörtgenin alanını ve çevresini hesaplayınız.
Daha sonra Dikdörtgenin Alanı: ….. Çevresi:……. şeklinde bir çıktı üretiniz  """

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
## farklı yazdırma stili, parametreli yazdırım
print("Alan : {0}".format(alan))
print("Çevre : {0}".format(cevre))

###############################################################
x=1;y=2;z=3
print("x değeri={0}, y değeri={1}, z değeri={2}".format(x,y,z))
###############################################################

print("Alan: {0}, Çevre: {1}".format(alan,cevre))