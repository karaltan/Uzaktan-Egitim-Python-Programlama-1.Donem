"""
yol=hız x zaman
formülüne göre dışarıdan girilen değerlerle yolu hesaplayınız
"""
# kaç kilometre hız ile gidiyorsun? kaç saattir yoldasın? yolu hesapla

hız=float(input("kaç kilometre hız ile gidiyorsun:"))
saat=float(input("kaç saattir yoldasın:"))

yol= hız*saat
print("Şu ana kadar {0} km yol yaptınz".format(yol))