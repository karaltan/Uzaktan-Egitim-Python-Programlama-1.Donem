
# maaş zam hesaplama
yeniMaas=0

maas=float(input("Maaşı Gir : "))
zam=float(input("Zam Oranı(%) : "))

zamoranı=maas*(zam/100)

yeniMaas=maas+zamoranı

print("Zamlı Maaş :",yeniMaas)
