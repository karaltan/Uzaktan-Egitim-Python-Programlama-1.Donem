import datetime
"""Kullanıcıya adını ve doğum tarihi sorunuz. Girilen doğum tarihine göre yaşını hesaplayınız. Aşağıdaki gibi
bir ekran çıktısı üretiniz.
Merhaba …(ad)……., yaşınız …….’dır"""

isim=input("isminizi giriniz:")
dogumyili=int(input("doğum yılınızı giriniz:"))

yas=2020-dogumyili
#bugun = datetime.datetime.today()
#print(bugun)
#yil=bugun.year
#yas=yil-dogumyili

print("Merhaba",isim,", yaşınız",yas," dır")



