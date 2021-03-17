ort = int(input("Ortalamayı Giriniz: "))
devam = int(input("Devamsızlıkğı Giriniz: "))

if ort<50 and devam<10:
    durum = "ortalamadan kaldı"
elif ort>50 and devam>10:
    durum = "devamsızlıktan kaldı"
elif ort<50 and devam>10:
    durum = "kaldı"
elif ort>50 and devam<10:
    durum = "geçti"
else:
    durum = "geçerli bir değer yazınız"

print(durum)





