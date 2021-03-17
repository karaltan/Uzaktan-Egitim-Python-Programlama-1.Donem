"""kullanıcının girdiği 3 sınav notuna göre ortalamayı hesaplayan ve ekrana yazdıran kodu yazınız.."""

#PROGRAMLARI YAZARKEN
#GİRİŞ : değişkenler tanımlanır, değerler alınır
#GELİŞME: işlemler, formüller yazılır
#SONUÇ: ekrana çıktı verilir
#bölümleri şeklinde yazarsak daha okunaklı olur

# input("1.sınav puanınızı giriniz:")
#GİRİŞ
puan1=float(input("1.sınav puanınızı giriniz:"))
puan2=float(input("2.sınav puanınızı giriniz:"))
puan3=float(input("3.sınav puanınızı giriniz:"))
#GELİŞME
ortalama=(puan1+puan2+puan3)/3 
#SONUÇ
print("ortalamanız:",ortalama)



