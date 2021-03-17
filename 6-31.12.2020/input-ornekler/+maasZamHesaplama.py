
# maaş zam hesaplama

#GİRİŞ
yeniMaas=0
maas=float(input("Maaşı Gir : "))
zam=float(input("Zam Oranı(%) : "))

#GELİŞME
# zam demek maaşa eklenen paradır
zamoranı=maas*(zam/100)
# hesaplanan zammı maaşa ekleyelim
yeniMaas=maas+zamoranı

#SONUÇ
print("Zamlı Maaş :",yeniMaas)
