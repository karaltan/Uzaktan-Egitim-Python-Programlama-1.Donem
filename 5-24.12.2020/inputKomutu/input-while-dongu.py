sayac=1
yastoplam=0

ogrencisayisi=int(input("Öğrenci sayısını giriniz="))

while sayac<=ogrencisayisi:
    # yas=int(input(str(sayac) +".öğrencinin yaşını gir="))
    # yas=int(input(f"{sayac}.öğrencinin yaşını gir="))
    yas=int(input("{0}.öğrencinin yaşını gir=".format(sayac)))
    sayac=sayac+1
    yastoplam=yastoplam+yas
    
yasortalama=yastoplam/ogrencisayisi
    
print("Öğrencilerin yaşları toplamı=",yastoplam)
print("Öğrencilerin yaşlarının ortalaması=",yasortalama)