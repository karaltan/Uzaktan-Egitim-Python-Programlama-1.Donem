"""
Kullanıcının girdiği kısa ve uzun kenar değerlerine göre;
dikdörtgenin alanını ve çevresini hesaplayınız.
Daha sonra Dikdörtgenin Alanı: ….. Çevresi:……. şeklinde bir çıktı üretiniz  """

#GİRİŞ
kisa=int(input("dikdörtgenin kısa kenarını giriniz:"))
uzun=int(input("dikdörtgenin uzun kenarını giriniz:"))

#GELİŞME
alan=kisa*uzun
#cevre=kisa+uzun+kisa+uzun
cevre=2*(kisa+uzun)

#SONUÇ
print("alan=",alan)
print("çevre=",cevre)
## farklı yazdırma stili, parametreli yazdırım
print("Alan : {0}".format(alan))
print("Çevre : {0}".format(cevre))

#parametreli çıktı#############################################
x=1;y=2;z=3
print("x değeri={0}, y değeri={1}, z değeri={2}".format(x,y,z))
###############################################################

print("Alan: {0}, Çevre: {1}".format(alan,cevre))