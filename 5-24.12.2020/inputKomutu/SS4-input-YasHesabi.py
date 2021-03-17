
"""Kullanıcıya adını ve doğum tarihi sorunuz. Girilen doğum tarihine göre yaşını hesaplayınız. Aşağıdaki gibi
bir ekran çıktısı üretiniz.
Merhaba …(ad)……., yaşınız …….’dır"""

import datetime

isim=input("isminizi giriniz:") # metinsel ifadeler direk yazılır

dogumyili=int(input("doğum yılınızı giriniz:")) # sayısal ifadelerde int kullanılır

yas=2020-dogumyili
#bugun = datetime.datetime.today()
#print(bugun)
#yil=bugun.year
#yas=yil-dogumyili

print("Merhaba",isim,", yaşınız:",yas," dır")



