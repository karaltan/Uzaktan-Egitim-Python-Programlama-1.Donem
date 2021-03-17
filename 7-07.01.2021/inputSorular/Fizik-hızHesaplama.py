"""
yol=hız x zaman
hız=yol/zaman
formülüne göre dışarıdan girilen değerlerle hızı hesaplayınız
"""
# kaç kilometre yol yaptın? kaç saattir yoldasın? hızı hesapla

yol=float(input("kaç kilometre yol yaptın:"))
saat=float(input("kaç saattir yoldasın:"))

hız= yol/saat
print("{0} km/saat hızla ilerliyorsun".format(hız))